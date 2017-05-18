def my_adder(a, b):
    return a + b


def test_my_adder():
    n = 1
    y = 10
    val = my_adder(n, y)
    if val != n + y:
        print 'my_adder is broken'


if __name__ == '__main__':
    test_my_adder()
