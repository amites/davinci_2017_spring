#!/usr/bin/python


class Beatles:
    var = 'my value'

    def __init__(self):
        self.sitting = 'in an English garden waiting for the sun'

    @classmethod
    def the_walrus(cls):
        print cls.var
        print cls.sitting
        print 'I am the walrus'

    @property
    def in_garden(self):
        return self.sitting

    def other_method(self):
        print 'I know about {}'.format(self.var)
        print 'and I know about {}'.format(self.sitting)

    @staticmethod
    def coo_coo():
        print 'coo coo cachoo ca coo coo cachoo'



