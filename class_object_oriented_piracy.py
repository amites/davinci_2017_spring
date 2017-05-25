# https://www.codewars.com/kata/object-oriented-piracy/train/python


class Ship(object):
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
        self.crew_weight = 1.5 * self.crew

    def is_worth_it(self):
        if self.draft - self.crew_weight > 20:
            return True
        else:
            return False
