# https://www.codewars.com/kata/most-digits/train/python

def find_longest(arr):
    length = 0
    position = 0
    for i in range(0, len(arr)):
        num_digits = len(str(arr[i]))
        if num_digits > length:
            position = i
            length = num_digits
    return arr[position]
