import pyaudio

p = pyaudio.PyAudio()
usb_mic_index = None

print("Available audio devices:")
for i in range(p.get_device_count()):
    dev_info = p.get_device_info_by_index(i)
    print(f"{i}: {dev_info['name']}, Input Channels: {dev_info['maxInputChannels']}")

    if 'USB Audio' in dev_info['name'] and dev_info['maxInputChannels'] > 0:
        usb_mic_index = i
        print(f"Found USB microphone at index {i}: {dev_info['name']}")

if usb_mic_index is not None:
    print(f"USB Microphone is at index {usb_mic_index}")
else:
    print("No USB microphone found. Please check your connection.")
    p.terminate()
    exit()

# Test recording from the USB microphone
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=44100,
                input=True,
                frames_per_buffer=1024,
                input_device_index=usb_mic_index)

print("Recording a short sample...")
frames = []
for _ in range(0, int(16000 / 1024 * 2)):  # Record for 2 seconds
    data = stream.read(1024, exception_on_overflow=False)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

print("Recording complete.")

