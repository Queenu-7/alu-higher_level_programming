#!/usr/bin/python3

def islower(c):
    """Check if the character c is lowercase"""
    return ord('a') <= ord(c) <= ord('z')

if __name__ == "__main__":
    # Simple tests when running this file directly
    test_chars = ['a', 'H', 'A', '3', 'g']
    for ch in test_chars:
        print(f"{ch} is {'lower' if islower(ch) else 'upper'}")
