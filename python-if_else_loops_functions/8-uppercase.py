#!/usr/bin/python3

def uppercase(str):
    result = ""
    for c in str:
        if 97 <= ord(c) <= 122:
            result += chr(ord(c) - 32)
        else:
            result += c
    print("{}".format(result))


# Example usage:
uppercase("best")
uppercase("Best School 98 Battery street")
