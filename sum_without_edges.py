# https://www.codewars.com/kata/sum-without-highest-and-lowest-number/train/python

def sum_array(arr):
    if not arr or len(arr) < 2:
        return 0
    arr.sort()
    my_num = 0
    for n in arr[1:-1]:
        my_num = my_num + n
    return my_num
