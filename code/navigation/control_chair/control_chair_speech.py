import sys
sys.path.insert(0, "/home/mosschair/navigation/nav-venv/lib/python3.6/site-packages")
import os
import time
import pyaudio
import string
import serial
from google.cloud import speech

# Setup the serial connection to Arduino
arduino_port = '/dev/ttyACM0'  # Adjust this port to match your setup
arduino_baudrate = 9600
arduino = serial.Serial(arduino_port, arduino_baudrate, timeout=1)

# Setup Google Cloud credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'mosschairkey.json'

# Initialize PyAudio
p = pyaudio.PyAudio()
input_device_index = 11
fs = 44100  # Using the original sampling rate

# Setup audio stream
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=fs,
                input=True,
                input_device_index=input_device_index,
                frames_per_buffer=int(fs * 0.02))

# Initialize Google Speech Client
client = speech.SpeechClient()
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=fs,
    language_code="en-US",
    enable_automatic_punctuation=True)
streaming_config = speech.StreamingRecognitionConfig(config=config, interim_results=True)

# Stream microphone input to the Speech-to-Text API with restart
def stream_microphone_with_restart():
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time >= 300:  # Restart stream after 5 minutes (300 seconds)
            break
        yield speech.StreamingRecognizeRequest(audio_content=stream.read(int(fs * 0.02), exception_on_overflow=False))

# Define the valid commands and their mapping to Arduino format
valid_commands = {"forward", "backward", "turn right", "turn left", "stop", "quit"}
command_mapping = {
    "forward": "forward",
    "backward": "backward",
    "turn right": "turnRight",
    "turn left": "turnLeft",
    "stop": "stop",
    "quit": "quit"
}

# Function to clean and check commands
def clean_command(command):
    return command.translate(str.maketrans('', '', string.punctuation))

def is_valid_command(command):
    for valid_command in valid_commands:
        if valid_command in command:
            return valid_command
    return None

# Function to send commands to the Arduino
def send_command_to_arduino(command):
    print("Sending command:", command)
    arduino.write((command + '\n').encode('utf-8'))

# Function to manage the entire streaming and command process
def manage_streaming():
    last_command = 'stop'
    try:
        while True:
            responses = client.streaming_recognize(streaming_config, stream_microphone_with_restart())
            for response in responses:
                for result in response.results:
                    if result.is_final:
                        command_text = clean_command(result.alternatives[0].transcript.strip().lower())
                        valid_command = is_valid_command(command_text)
                        if valid_command:
                            formatted_command = command_mapping[valid_command]
                            if formatted_command != last_command:
                                last_command = formatted_command
                                print("Detected command:", last_command)
                                send_command_to_arduino(last_command)
            # Restart the stream by reinitializing the iterator
            print("Restarting stream to avoid 305-second limit")
    except KeyboardInterrupt:
        print("Manually interrupted by user")
    finally:
        # Cleanup
        stream.stop_stream()
        stream.close()
        p.terminate()
        arduino.close()

# Start the streaming and command processing
manage_streaming()

