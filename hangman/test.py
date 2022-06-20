
from ctypes.wintypes import CHAR
import random

while True:
            try:
                letter = input("Enter a letter: ")
                if len(letter) != 1:
                    print("Please, enter just one character")
            except:
                print("An exception occured")