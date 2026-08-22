#!/usr/bin/python3
def uppercase(str):
    final = ""
        if ord(char) >= 97 and ord(char) <= 122:
            final += chr(ord(char)- 32)
        else:
            final += char
        print("{}".format(final))
