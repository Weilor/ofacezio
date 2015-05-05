# -*- coding: utf-8 -*-
__author__ = '绍文'

import os
import re

filelist = os.listdir("C:\\Users\\绍文\\Pictures\\wallpaper")
for file in  filelist:
    if(re.match(r'\.jpg$', file, re.I)):
        picname = file
