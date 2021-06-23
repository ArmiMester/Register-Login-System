from simple_term_menu import TerminalMenu

def register():
	db = open("database.txt", "r")

	Username = input("Create username: ")
	Password = input("Create password: ")
	Password1 = input("Confirm password: ")

	if Password != Password1:
		print("Passwords doesn't match!")
	else:
		if len(Password) <= 6:
			print("Too short")
		elif Username in db:
			print("Username already exsist")
		else:
			db = open("database.txt", "a")
			db.write(Username + ", " + Password + "\n")
			print("Success!")

def login():
	db = open("database.txt", "r")
	Username = input("Enter username: ")
	Password = input("Enter password: ")

	if not len(Username or Password) < 1:
		if True:
			db = open("database.txt", "r")
			d = []
			f = []
			for i in db:
				a,b = i.split(",")
				b = b.strip()
				c = a,b
				d.append(a)
				f.append(b)
			data = dict(zip(d, f))
		try:
			if data[Username]:
				try:
					if Password == data[Username]:
						print("Login success!")
						print("Hello ", Username)
					else:
						print("Password or username are incorrect")
				except:
					print("Incorrect password or username")
			else:
				print("Username doesn't exsist")
		except:
			print("Username or password doesn't exsist")
	else:
		print("Enter a value")

def home():
	Chose = ["Login", "Register"]
	terminal_menu = TerminalMenu(Chose)
	choice_index = terminal_menu.show()

	if choice_index == 0:
		login()
	elif choice_index == 1:
		register()
	else:
		print("You are doing something very wrong")
home()
