# https://www.codewars.com/kata/reduce-my-fraction/train/python

# version 1
# worked but timed out (took toolong ot run) in tests

def reduce(fraction):
    numerator = fraction[0]
    denominator = fraction[1]
    if numerator > denominator:
        lower_number = denominator
    else:
        lower_number = numerator
    for n in range(lower_number, 0, -1):
        if numerator % n == 0 and denominator % n == 0:
            return [numerator / n, denominator / n]
        else:
            n += 1



# Version 2

# the reference that got the math figured out
# https://codereview.stackexchange.com/questions/66450/simplify-a-fraction

def reduce(fraction):
    numerator = fraction[0]
    denominator = fraction[1]
    if numerator > denominator:
        lower_number = denominator
        higher_number = numerator
    else:
        lower_number = numerator
        higher_number = denominator

    while higher_number:
        hold = lower_number
        lower_number = higher_number
        higher_number = hold % higher_number

    return [numerator / lower_number, denominator / lower_number]
