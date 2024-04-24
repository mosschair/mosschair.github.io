import serial
import curses
import time

# Initialize the serial connection to the Arduino
arduino = serial.Serial('/dev/ttyACM0', 9600)  # Adjust as needed

def send_command(command):
    arduino.write(command.encode())

def control_motors(stdscr):
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.nodelay(True)  # Non-blocking mode

    last_key = None
    last_time = time.time()

    while True:
        key = stdscr.getch()
        current_time = time.time()

        if key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
            if key != last_key or current_time - last_time >= 0.1:
                if key == curses.KEY_UP:
                    send_command('forward\n')
                elif key == curses.KEY_DOWN:
                    send_command('backward\n')
                elif key == curses.KEY_LEFT:
                    send_command('turnLeft\n')
                elif key == curses.KEY_RIGHT:
                    send_command('turnRight\n')
                else:
                    send_command('quit\n')
                last_time = current_time
        elif key == -1 and last_key is not None and current_time - last_time >= 0.1:
            send_command('stop\n')
            last_time = current_time
            last_key = None
        last_key = key if key != -1 else last_key
        time.sleep(0.01)  # Reduced sleep time for quicker response

    curses.nocbreak()
    stdscr.keypad(False)
    stdscr.nodelay(False)

def main():
    curses.wrapper(control_motors)
    arduino.close()

if __name__ == "__main__":
    main()

