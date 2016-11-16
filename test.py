import unittest

class Testdef(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello(), "hello world?!")
    def test_add(self):
        self.assertEqual((2, 4).add(), 6)

    def square(self):
        self.assertEqual(4.square(), 16)

if __name__ == '__main__':
    unittest.mail()
