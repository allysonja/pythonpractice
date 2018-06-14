import datetime

name = input("What is your name?: ")
age = int(input("What is your age?: "))
repeat = int(input("How many times should I repeat your message?: "))

age100 = datetime.datetime.now().year - age + 100

for i in range(0, repeat):
	print("Hello " + name + "! You will turn 100 years old in the year " + str(age100) + ".")