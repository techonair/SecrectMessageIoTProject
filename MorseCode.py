import requests  # for making HTTP requests
import json  # library for handling JSON data
import time  # module for sleep operation

from boltiot import Bolt  # importing Bolt from boltiot module
import conf  # config file

mybolt = Bolt(conf.bolt_api_key, conf.device_id)

# Python program to implement Morse Code Translator

'''
VARIABLE KEY
'cipher' -> 'stores the morse translated form of the english string'
'decipher' -> 'stores the english translated form of the morse string'
'citext' -> 'stores morse code of a single character'
'i' -> 'keeps count of the spaces between morse characters'
'message' -> 'stores the string to be encoded or decoded'
'''

# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':

            # Looks up the dictionary and adds the
            # correspponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '

    return cipher

# Function to decrypt the string
# from morse to english
def decrypt(message):

    # extra space added at the end to access the
    # last morse code
    message += ' '

    decipher = ''
    citext = ''
    for letter in message:

        # checks for space
        if (letter != ' '):

            # counter to keep track of space
            i = 0

            # storing morse code of a single character
            citext += letter

        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1

            # if i = 2 that indicates a new word
            if i == 2 :

                # adding space to separate words
                decipher += ' '
            else:

                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(citext)]
                citext = ''

    return decipher

# Hard-coded driver function to run the program
def main():
    message = "I LOVE YOU"
    global result
    result = encrypt(message.upper())
    print (result)


    message = "..  .-.. --- ...- .  -.-- --- ..-"
    result2 = decrypt(message)
    print (result2)

# Executes the main function
if __name__ == '__main__':
    main()


def wake_bolt_buzzer(pin):
    """Returns status of bolt and also alarms for new message arrival. Returns -999 if request fails"""
    try:
        response = mybolt.analogWrite(pin,150)
        data = json.loads(response)
        if data["success"] != 1:
            print("Request not successful")
            print("This is the response->", data)
            return -999
        response == mybolt.analogWrite(pin, 0)
        time.sleep(2)
        return print("Bolt detected ON")
    except Exception as e:
        print("Offline detected, check again")
        print(e)
        return -999

#calling wake_bolt_buzzer function to turn alarm the receiver via Bolt Buzzer
wake_bolt_buzzer(0)

def ledCode():
    """ Coding morse code into digital string codes """
    global blink
    blink= str(result)
    blink=blink.replace('-','1')
    blink=blink.replace('.','0')
    skips= [' ']
    for ch in skips :
        blink=list(blink) #.replace(ch,""))
    print(blink)

ledCode()

i=0

for blink[i] in blink:
    #led turns ON for 1 or (-) and OFF for 0 or (.), simultaneously buzzer alarms for every new character data
    try:
        if blink[i] == '1':
            print("it is a 1")
            buzzerOn = mybolt.analogWrite(0,50)
            ledON = mybolt.digitalWrite('1','HIGH')
            time.sleep(1)
            buzzerOff = mybolt.analogWrite(0,0)
            time.sleep(1)
            ledOff = mybolt.digitalWrite('1','LOW')
            i = i+1
            continue

        if blink[i] == '0':
            print('it is a 0')
            buzzerOn = mybolt.analogWrite(0,50)
            ledON = mybolt.digitalWrite('1','LOW')
            time.sleep(1)
            buzzerOff = mybolt.analogWrite(0,0)
            time.sleep(1)
            i = i+1
            ledOff = mybolt.digitalWrite('1','LOW')
            continue

        else:
            print("give space here") #*Two spaces* means space between two words while *one space* means next letter of same word
            buzzerOn = mybolt.analogWrite(0, 50  )
            ledON = mybolt.digitalWrite('4', 'HIGH')
            time.sleep(1)
            buzzerOff = mybolt.analogWrite(0, 0)
            time.sleep(1)
            ledOff = mybolt.digitalWrite('4', 'LOW')
            i = i + 1
            continue

    except Exception as e:
        print("Something went wrong when connecting")
        print(e)



