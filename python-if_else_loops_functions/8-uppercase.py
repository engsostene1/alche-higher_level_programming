#!/usr/bin/python3
def uppercase(str):
    s = "{}".format(str)
    result = ""
    for c in s:
        if 'a' <= c <= 'z':
            result += chr(ord(c) - 32)
        else:
            result += c
    print("{}".format(result))
