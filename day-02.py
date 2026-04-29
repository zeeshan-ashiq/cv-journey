# day-02.py
# Ask for a number , tells if positive/negative/zero and even/odd

number = int(input("enter a number: "))

#check positive , negative, or zero
if number > 0:
    print("the number is positive")
elif number < 0:
    print("the number is negative")
else:
    print ("the number is zero") 
# check even or odd   (only if not zero)
if number != 0:
    if number % 2 == 0:
        print ("the number is even")
    else:
        print("the number is odd")         