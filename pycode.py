import datetime

name = input("What is your name?: ")
age = int(input("What is your age?: "))

age100 = datetime.datetime.now().year - age + 100

print("Hello " + name + "! You will turn 100 years old in the year " + str(age100) + ".")