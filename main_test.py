import unittest

from main import hello_world


class TestMain(unittest.TestCase):
    def test_hello(self):
        ret = hello_world()
        self.assertEqual(ret, "Hello")


if __name__ == "__main__":
    unittest.main()
