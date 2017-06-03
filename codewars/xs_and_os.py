https://www.codewars.com/kata/exes-and-ohs/train/python

# version 1
def xo(s):
    s = s.lower()
    s.count('o')
    s.count('x')
    os = s.count('o')
    xs = s.count('x')
    return os == xs


# version 2
def xo(s):
    s = s.lower()
    return s.count('o') == s.count('x')



# version 3
def xo(s):
    return s.lower().count('o') == s.lower().count('x')
