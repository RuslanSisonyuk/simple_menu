#simple menu.
#now with *math!*
#and Passing functions as variables!
#
#work with numbers from user input
#save operation and result history
#
#

import math

def read_one_var():
	var = input("\nNumber: ")
	return var

def read_two_vars():
	var1 = int(input("\nFirst number: "))
	var2 = int(input("Second number: "))
	return var1,var2


def addition(numbers):
	return numbers[0] + numbers[1]

def subtraction(numbers):
	return numbers[0] - numbers[1]

def multiply(numbers):
	return numbers[0] * numbers[1]

def division(numbers):
	return numbers[0] / numbers[1]

def round_number(number):
	return

def


def execute_option_type1(func,symbol):
	numbers = read_two_vars()
	print(f"\n{numbers[0]} {symbol} {numbers[1]} = {func(numbers)}\n")
	input("/Back to menu/")
	menu()

def execute_option_type2(func):
	number = read_one_var()

	input("/Back to menu/")
	menu()


def menu():
		print("Options:")
		print(
			"1: Addition\n"
			"2: Subtraction\n"
			"3: Multiplication\n"
			"4: Division\n"
			"5: Round number\n"
			"6: Square root")

		user_input = input("\nEnter option: ")
		match user_input:
			case "0":
				print("Closing menu")
				return 0
			case "1":
				execute_option_type1(addition,'+')
			case "2":
				execute_option_type1(subtraction,'-')
			case "3":
				execute_option_type1(multiply,'*')
			case "4":
				execute_option_type1(division,'/')
			case "5":
				menu()
			case "6":
				menu()
			case _:
				menu()
	
def main():
	menu()

if __name__ == "__main__":
	main()