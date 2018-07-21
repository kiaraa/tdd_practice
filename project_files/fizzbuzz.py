'''
Write a program that prints the numbers from 1 to 100. But for multiples of three print Fizz
instead of the number and for the multiples of five print Buzz. For numbers which are multiples
of both three and five print FizzBuzz
'''

class FizzBuzz(object):

    def turn_int_into_string(self, number):
        if number % 3 == 0 and number % 5 == 0:
            return "FizzBuzz"
        elif number % 3 == 0:
            return "Fizz"
        elif number % 5 == 0:
            return "Buzz"
        else:
            return str(number)

    def print_all_values(self):
        for x in range(1,101):
            string_to_print = self.turn_int_into_string(x)
            print(string_to_print)

if __name__ == '__main__':
    FizzBuzz().print_all_values()