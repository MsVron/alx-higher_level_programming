#!/usr/bin/python3

#!/usr/bin/python3

def uppercase(str):
    result = ""
    for c in str:
        if 'a' <= c <= 'z':
            c = chr(ord(c) - ord('a') + ord('A'))
        result += c
    print("{}".format(result))
