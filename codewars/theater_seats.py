# https://www.codewars.com/kata/simple-fun-number-1-seats-in-theater/train/python

# Version 1
def seats_in_theater(tot_cols, tot_rows, col, row):
    blocked_column = tot_cols - col
    blocked_rows = tot_rows - row
    return blocked_column * blocked_rows


# Version 2
def seats_in_theater(tot_cols, tot_rows, col, row):
    return (tot_cols - col + 1) * (tot_rows - row)
