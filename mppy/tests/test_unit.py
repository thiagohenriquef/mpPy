import unittest

def fun(x):
    """
    basic function for test
    :param x: value
    :return: value incremented with 1
    """
    return x + 1

class MyTest(unittest.TestCase):
    """
    Simple class to unit test
    """
    def test(self):
        self.assertEqual(fun(3), 4)

if __name__ == '__main__':
    unittest.main()