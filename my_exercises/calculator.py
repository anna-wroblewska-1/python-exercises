#calculator
#input 2 digits
#choose oprator (addition, subtraction, multiplication, division)
#give result

x = input("Give first number: ")
x=int(x)
print(x)

y = input("Give second number: ")
y=int(y)
print(y)


operator = input(f"Choose the operator + - / * : ")
if operator == "+":
    print(x+y)
if operator == "-":
    print(x-y)
if operator == "/":
    print(x/y)  
    if y == 0:
        print("You can't divide by 0")
if operator == "*":
    print(x*y) 
else:
    print("Choose wisely")