import serial, time, sys, getopt

baud = 9600
port = 'COM3'
arduino = serial.Serial(port, baud, timeout=1)

def sendToArduino(data):
    val = arduino.write(str.encode(data))
    time.sleep(0.001)
    return val

def readFromArduino():
    return arduino.read()

def readEEPROM():
    time.sleep(5)        
    arduino.write(str.encode('r'))
    time.sleep(0.5)

    while True:
        data = arduino.readline()
        if data:
            for i in range(17):
                print(data)
                data = arduino.readline()
            break

def writeEEPROM(inputfile):
    hexL = []
    with open(inputfile, "rb") as f:
        n = 0
        b = f.read(16)
        while b:
            s1 = " ".join([f"{i:02x}" for i in b]) # hex string
            for i in b:
                #hexL.append(f"{i:02x}")
                hexL.append(i)
            s1 = s1[0:23] + " " + s1[23:]          # insert extra space between groups of 8 hex values
            s2 = "".join([chr(i) if 32 <= i <= 127 else "." for i in b]) # ascii string; chained comparison
            print(f"{n * 16:08x}  {s1:<48}  |{s2}|")
            n += 1
            b = f.read(16)              
    time.sleep(5)        
    arduino.write(str.encode('w'))
    time.sleep(0.5)
    for i in hexL:
        #print(i.to_bytes(1, byteorder="little"))
        arduino.write(i.to_bytes(1, byteorder="little"))
    
    
def wrEEPROM(inputfile):
    print("Writing and Reading EEPROM...")
    writeEEPROM(inputfile)
    time.sleep(1)
    readEEPROM()

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
            readEEPROM()
        elif current_argument in ("-w", "--write"):
            writeEEPROM(current_value)
        elif current_argument in ("-t", "--writeread"):
            wrEEPROM(current_value)

    time.sleep(1)
    arduino.close()
    

if __name__ == "__main__":
    main(sys.argv[1:])



    
