import sys
import os
import time
import threading
import pyaudio
import string
from google.cloud import speech


last_command = 'stop'
command_lock = threading.Lock()

def send_command(command):
    with command_lock:
        print("Sending command:", command)

# Function to continuously print the last command every 0.01 seconds
def print_last_command():
    global last_command
    while True:
        with command_lock:
            current_command = last_command
        send_command(current_command)
        time.sleep(0.01)  # Command print interval

# Setup Google Cloud credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'mosschairkey.json'

# Initialize PyAudio
p = pyaudio.PyAudio()
input_device_index = 11
fs = 44100

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
    sample_rate_hertz=fs,  # Set this to 48000 Hz
    language_code="en-US",
    enable_automatic_punctuation=True)
streaming_config = speech.StreamingRecognitionConfig(config=config, interim_results=True)

# Stream microphone input to the Speech-to-Text API without resampling
def stream_microphone():
    while True:
        yield speech.StreamingRecognizeRequest(audio_content=stream.read(int(fs * 0.02), exception_on_overflow=False))

# Define valid commands
valid_commands = {"forward", "backward", "turn right", "turn left", "stop"}

# Function to clean and check commands
def clean_command(command):
    # Remove punctuation from the command for better matching
    return command.translate(str.maketrans('', '', string.punctuation))

def is_valid_command(command):
    # Check if any valid command is in the spoken phrase
    for valid_command in valid_commands:
        if valid_command in command:
            return valid_command
    return None

# Start the thread that prints the last command
print_thread = threading.Thread(target=print_last_command, daemon=True)
print_thread.start()

try:
    responses = client.streaming_recognize(streaming_config, stream_microphone())
    for response in responses:
        for result in response.results:
            if result.is_final:
                command = clean_command(result.alternatives[0].transcript.strip().lower())
                valid_command = is_valid_command(command)
                if valid_command and valid_command != last_command:
                    last_command = valid_command
                    print("Detected command:", last_command)
                    send_command(last_command)
                elif not valid_command:
                    print("No valid command detected.")
except KeyboardInterrupt:
    print("Manually interrupted by user")
finally:
    # Cleanup
    stream.stop_stream()
    stream.close()
    p.terminate()

