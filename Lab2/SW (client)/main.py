import serial
import time

arduino = serial.Serial(port='COM6', baudrate=9600, timeout=.1)

def communicate_with_arduino(data):
    for char in data:
        arduino.write(char.encode(encoding='ascii'))
        time.sleep(.1)
    data = ''
    while True:
        response = arduino.readline()
        if response != b'':
            data += response.decode()

        if ';' in data:
            break
    return data.replace('\r\n', '')

def main():
    message = '    Dmytro;'
    print('Message to Arduino:', message.strip())
    print('Message from Arduino:',  communicate_with_arduino(message))

if __name__ == "__main__":
    main()