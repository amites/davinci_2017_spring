# https://www.codewars.com/kata/interactive-dictionary/train/python


class Dictionary():
    def __init__(self):
        self.d = {}

    def newentry(self, word, definition):
        self.d[word] = definition

    def look(self, key):
        return self.d.get(key, "Can't find entry for {}".format(key))


# >>> d = Dictionary()
# >>> d.newentry('Apple', 'A fruit that grows on trees')
# >>> print(d.look('Apple'))
# A fruit that grows on trees
# >>> print(d.look('Banana'))
# Cant find entry for Banana
