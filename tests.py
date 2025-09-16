import unittest
from string_utils import *
from generator import *

class TestSimpleFunctions(unittest.TestCase):

    def test_print_string(self):
        self.assertEqual(print_string("Hello"), "Hello")
        self.assertEqual(print_string(123), "Помилка: функція приймає тільки рядки!")

    def test_check_case(self):
        self.assertEqual(check_case("HELLO"), "Всі великі")
        self.assertEqual(check_case("hello"), "Всі малі")
        self.assertEqual(check_case("HeLlo"), "Змішані")
        self.assertEqual(check_case(123), "Помилка: функція приймає тільки рядки!")

    def test_to_upper_list(self):
        self.assertEqual(to_upper_list("smogtether"), ["S","M","O","G","T","E","T","H","E","R"])

    def test_even_odd(self):
        gen = even_odd()
        self.assertEqual(next(gen), "Парне")
        self.assertEqual(next(gen), "Непарне")

if __name__ == "__main__":
    unittest.main()