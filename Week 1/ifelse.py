#inputing the 2 numbers
x = int(input("First number: "))
y = int(input("Second number: "))

def greater(a, b):
    if a > b:
        print(str(a) + " is the greater number.")
    elif b > a:
        print(str(b) + " is the greater number.")
    else:
        print("They are equal.")

greater(x,y)