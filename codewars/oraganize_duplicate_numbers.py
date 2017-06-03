# https://www.codewars.com/kata/organise-duplicate-numbers-in-list/train/python


def group(arr):
    new_arr = []  # define new list to return
    while True:  # keep looping through the original list until we break
        if len(arr) == 0:  # when original list is empty stop
            break
        vals = [arr[0], ]  # create new sub-list container
        del arr[0]  # remove the value now in sub-list from original list
        while True:  # loop through the original list looking for matches
            try:  # look for the next match
                position = arr.index(vals[0])  # get the position of the next match of our current number
            except ValueError:  # if no match then stop current loop
                break
            vals.append(arr[position])  # add the next match to our sub-list
            del arr[position]  # remove the next match from original list
        new_arr.append(vals)  # add the sub-list to the original list
    return new_arr  # spit back the new list of sub-list's
