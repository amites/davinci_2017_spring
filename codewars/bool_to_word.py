# https://www.codewars.com/kata/convert-boolean-values-to-strings-yes-or-no/train/python

def bool_to_word(bool):
    yes_str = 'Yes'
    no_str = 'No'
    if bool:
        return yes_str
    else:
        return no_str
