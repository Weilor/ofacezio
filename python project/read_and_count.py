__author__ = '绍文'
from string import punctuation
import re

fp = open("zenofpython.txt", "r")       # open text file
string_list = fp.readlines()            # read all line from file
word_list = {}
for string in string_list:
    word = string.split(" ")            # slit lines whit space, then i can get all single word
    for word_single in word:
        wd = re.sub(r'[{}]+'.format(punctuation), '', word_single.strip())   # remove punctuation from word
        if wd in word_list.keys():
            word_list[wd] += 1          # count every word
        else:
            word_list[wd] = 1
for k, v in word_list.items():
    print(k, "count", v)