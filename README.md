# Arduino EEPROM programmer

A simple Python3 script to read/program your EEPROMs without the needs of an EEPROM programmer.

Version: 0.0.1a
Date: 23/05/20

## Installation

Clone the repository on your machine. Upload the Arduino script into your Arduino (see Configuration), and you are ready.

## Arduino connections

The connections between Arduino and the EEPROM are the same as deeply described by [Ben Eater](https://github.com/beneater/eeprom-programmer) in his repository. Huge shout out to the guy!

## Configuration

A little configuration stage is needed for the Python script:

1. At the top, modify the `port` variable with your Arduino connection port. 
(OPTIONAL)
2. You can change the `baud` for the serial connection, but be sure to be consistent in the Arduino script as well.  

## Usage

`python3 eepyrom.py <options> <parameters>`

Currently the script accepts three options:

* `python3 eepyrom.py -r ` : prints the content of the EEPROM
* `python3 eepyrom.py -w ./file.txt `: reads the file.txt, translate it into hex and write the content in the EEPROM
* `python3 eepyrom.py -wr ./file.txt `: writes the file.txt into the EEPROM, and then reads its content

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
