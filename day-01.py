# day-01.py
# my first python program
# asks for name and age, prints a greeting
name = input("what is your name? ")
age = input("how old are you?")
#convert age from string to intiger 
age_number = int(age)
#calculate age in 10 years 
future_age = age_number + 10
#print the greeting
print("hello " + name + ", in 10 years you will be " + str(future_age))