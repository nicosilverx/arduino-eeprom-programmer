import serial, time, sys, getopt
from serial.serialutil import to_bytes

baud = 9600
port = 'COM3'
arduino = serial.Serial(port, baud, timeout=1)

def sendToArduino(data):
    val = arduino.write(str.encode(data))
    time.sleep(0.001)
    return val

def readFromArduino():
    return arduino.read()

def main(argv):
    short_options = "hrw:t:"
    long_options = ["help","write=","read","writeread="]

    cmd = ''

    if len(sys.argv) < 2:
        print("Not enough argoument. Use --help.")
        sys.exit(2)

    try:
        arguments, values = getopt.getopt(argv, short_options, long_options)
    except getopt.GetoptError as err:
        print("test.py -w <string>", err)
        sys.exit(2)

    for current_argument, current_value in arguments:
        if current_argument in ("-h", "--help"):
            print("HELP GUIDE")
            sys.exit()
        elif current_argument in ("-r", "--read"):
            cmd = 'r'
        elif current_argument in ("-w", "--write"):
            cmd = 'w'
        elif current_argument in ("-t", "--writeread"):
            cmd = 't'

    time.sleep(1)

    print("String to be sent to Arduino: ", cmd)
    
    
    sendToArduino(cmd)
    print(arduino.readline())
    #sendToArduino(cmd)
    print(arduino.readline())
    sendToArduino(cmd)
    print(arduino.readline())

    while True:
        data = arduino.readline(100)
        print(data)
        
    arduino.close()
    

if __name__ == "__main__":
    main(sys.argv[1:])



    
