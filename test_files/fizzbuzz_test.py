'''
Write a program that prints the numbers from 1 to 100. But for multiples of three print Fizz
instead of the number and for the multiples of five print Buzz. For numbers which are multiples
of both three and five print FizzBuzz
'''
import unittest

from project_files.fizzbuzz import FizzBuzz
import builtins


class MockPrint():

    def __init__(self):
        self.number_of_calls = 0
        self.called_with = []

    def print(self, value):
        self.number_of_calls += 1
        self.called_with.append(value)

    def how_many_times_called(self):
        return self.number_of_calls

    def called_with_values(self):
        return self.called_with



class TestFizzBuzz(unittest.TestCase):

    def setup_method(self, method):
        self.fizzbuzz = FizzBuzz()
        self.mock_printer = MockPrint()
        builtins.print = self.mock_printer.print


    def test_return_7_as_string_when_given_7(self):
        result = self.fizzbuzz.turn_int_into_string(7)
        self.assertEqual(result, "7")

    def test_return_1_as_string_when_given_1(self):
        result = self.fizzbuzz.turn_int_into_string(1)
        self.assertEqual(result, "1")

    def test_return_fizz__when_given_3(self):
        result = self.fizzbuzz.turn_int_into_string(3)
        self.assertEqual(result, "Fizz")

    def test_return_fizz_when_given_9(self):
        result = self.fizzbuzz.turn_int_into_string(9)
        self.assertEqual(result, "Fizz")

    def test_return_buzz_when_given_5(self):
        result = self.fizzbuzz.turn_int_into_string(5)
        self.assertEqual(result, "Buzz")

    def test_return_buzz_when_given_20(self):
        result = self.fizzbuzz.turn_int_into_string(20)
        self.assertEqual(result, "Buzz")

    def test_return_fizzbuzz_when_given_15(self):
        result = self.fizzbuzz.turn_int_into_string(15)
        self.assertEqual(result, "FizzBuzz")

    def test_return_fizzbuzz_when_given_60(self):
        result = self.fizzbuzz.turn_int_into_string(60)
        self.assertEqual(result, "FizzBuzz")

    def test_actually_prints(self):
        self.fizzbuzz.print_all_values()
        self.assertEqual(self.mock_printer.how_many_times_called(), 100)
        values_called_with = self.mock_printer.called_with_values()
        self.assertEqual(values_called_with[0], "1")
        self.assertEqual(values_called_with[1], "2")
        self.assertEqual(values_called_with[2], "Fizz")
        self.assertEqual(values_called_with[3], "4")
        self.assertEqual(values_called_with[4], "Buzz")
        self.assertEqual(values_called_with[-1], "Buzz")
