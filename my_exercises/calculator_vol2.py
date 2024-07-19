#calculator v.2


def adddition(x, y):
    print(x+y)

def substraction(x, y):
    print(x-y)

def division(x, y):
    print(x/y)
    if y == 0:
        print("You can't divide by 0")

def multiplication(x, y):
    print(x*y)

x = int(input("Give first number: "))
print(x)

operator = input("Choose operator + - / *: ")

y = int(input("Give second number: "))
print(y)

if operator == "+":
    adddition(x, y)
elif operator == "-":
    substraction(x, y)
elif operator == "/":
    division(x, y)  
elif operator == "*":
    multiplication(x, y)
else:
    print("Choose wisely")