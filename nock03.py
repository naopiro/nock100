# coding: UTF-8
# 行数のカウント

import sys

with open(sys.argv[1]) as f:
    str = f.read()

print(str.replace("\t"," "))


