import unittest
import sortlines


class TestStringMethods(unittest.TestCase):

    def test_upper(t):
        input = "c\na\nb"
        expect = "a\nb\nc"
        reality = sortlines.sortLines(input)
        t.assertEqual(expect, reality)


if __name__ == '__main__':
    unittest.main()
