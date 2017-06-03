# https://www.codewars.com/kata/simple-fun-number-132-number-of-carries/train/python

def number_of_carries(a, b):

    y = [int(n) for n in list(str(a))]
    x = [int(n) for n in list(str(b))]

    # reverse order so beginning with smallest
    # and going to biggest
    y.reverse()
    x.reverse()

    # figure out which list contains more digits
    if a > b:
        longer = y
        shorter = x
    else:
        longer = x
        shorter = y

    # define starting values
    carry = 0
    count = 0

    for i in range(0, len(longer)):

        # skip adding from a column that does not exist
        if i < len(shorter):
            num = longer[i] + shorter[i] + carry
        else:
            num = longer[i] + carry

        if num > 9:
            count += 1
            carry = 1
        else:
            carry = 0
    return count
