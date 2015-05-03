__author__ = '绍文'
from string import punctuation
import re

fp = open("zenofpython.txt", "r")       # open text file
string = fp.read()
word = re.findall(r'[a-zA-z0-9]+', string)

if __name__ == "__main__":
    print(len(word))