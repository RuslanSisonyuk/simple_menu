#simple menu.
#now with *math!*
#and Passing functions as variables!
#
#work with numbers from user input
#save operation and result history
#
#

import math

class stored_operation:
	def __init__(self,values,operation,result):
		self.values = values
		self.operation = operation
		self.result = result


def read_one_var():
	var = float(input("\nNumber: "))
	return var,0

def read_two_vars():
	var1 = float(input("\nFirst number: "))
	var2 = float(input("Second number: "))
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
	return math.floor(number)

def power2(number):
	return pow(number,2)

def store_operation(numbers,operation,result):
	op = stored_operation(numbers,operation,result)
	return op

def view_op_history(op_history):
	for op in op_history:
		if(op.operation == '^'):
			print(f"\n{op.values[0]} ^ 2 = {op.result}")
		elif(op.operation == "~"):
			print(f"\n{op.values[0]} ~= {op.result}")
		else:
			print(f"\n{op.values[0]} {op.operation} {op.values[1]} = {op.result}")
	input("//Continue//")

def execute_option(op_history,func,symbol):
	if(symbol == '^' or symbol == '~'):
		numbers = read_one_var()
		result = func(numbers[0])
		print(f"\n{numbers[0]} {symbol} = {result}\n")
	else:
		numbers = read_two_vars()
		result = func(numbers)
		print(f"\n{numbers[0]} {symbol} {numbers[1]} = {result}\n")
	op_history.append(stored_operation(numbers,symbol,result))
	input("/Back to menu/")
	menu(op_history)

def menu(op_history):
		print("Options:")
		print(
			"1: Addition\n"
			"2: Subtraction\n"
			"3: Multiplication\n"
			"4: Division\n"
			"5: Round number\n"
			"6: Square root\n"
			"7: View history\n"
			"0: Exit")

		user_input = input("\nEnter option: ")
		match user_input:
			case "0":
				print("Closing menu")
				exit(1)
			case "1":
				execute_option(op_history,addition,'+')
			case "2":
				execute_option(op_history,subtraction,'-')
			case "3":
				execute_option(op_history,multiply,'*')
			case "4":
				execute_option(op_history,division,'/')
			case "5":
				execute_option(op_history,round_number,'~')
			case "6":
				execute_option(op_history,power2,'^')
			case "7":
				view_op_history(op_history)
				menu(op_history)
			case _:
				menu(op_history)
	
def main():
	op_history=[]
	menu(op_history)

if __name__ == "__main__":
	main()