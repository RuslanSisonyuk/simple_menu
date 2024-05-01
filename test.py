#simple menu.

def menu():
	user_input = input("\nEnter option: ")
	match user_input:
		case "0":
			print("Closing menu")
			return 0
		case "1":
			print("You pressed 1!")
			menu()
		case "2":
			print("That's not 1!")
			menu()
		case _:
			print("lmao")
			menu()

menu()