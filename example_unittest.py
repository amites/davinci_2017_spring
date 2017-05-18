import unittest

from example_test import my_adder


class TestMyAdder(unittest.TestCase):
    def test_my_adder(self):
        for n in xrange(5):
            val = my_adder(n, 10, False)
            self.assertEqual(val, n + 10)


if __name__ == '__main__':
    unittest.main()
