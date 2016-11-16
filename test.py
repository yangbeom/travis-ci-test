import unittest
import hello

class Testdef(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello.hello(), "hello world?!")
    def test_add(self):
        self.assertEqual(hello.add(2, 4), 6)

    def square(self):
        self.assertEqual(hello.square(4), 16)

if __name__ == '__main__':
    unittest.main()
