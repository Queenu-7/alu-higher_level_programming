#!/usr/bin/python3

def uppercase(str):
    for c in str:
        # Check if character is lowercase letter a-z
        if ord('a') <= ord(c) <= ord('z'):
            # Convert to uppercase by subtracting 32
            print("{}".format(chr(ord(c) - 32)), end="")
        else:
            print("{}".format(c), end="")
    print()  # Newline at the end

if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
