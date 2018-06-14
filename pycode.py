import datetime

name = input("What is your name?: ")
age = int(input("What is your age?: "))

age100 = datetime.datetime.now().year - age + 100
print(age100)