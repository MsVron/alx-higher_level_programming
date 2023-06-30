#!/usr/bin/python3

alphabet = ""

for char_code in range(ord('a'), ord('z')+1):
    alphabet += chr(char_code)

print("{}{}".format(alphabet, ''), end='')
