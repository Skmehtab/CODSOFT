#funtion to add two numbers
def ADD(x, y):
    return x+y
#function to subtract two numbers
def SUB(x, y):
    return x-y
#function to multiply two numbers
def MULT(x, y):
    return x*y
#function to divide two numbers
def DIV(x, y):
    if y==0:
        return "Operaion Error, cannot divide by 0"
    else:
        return x/y

#selecting operation to perform
print("Select an arithmetic operation to perform:\n"
      "1. ADDITION\n" \
      "2. SUBTRACTION\n" \
      "3. MULTIPLICATION\n" \
      "4. DIVISION\n")

#taking inputs from user
while True:
    choice=int(input("Select operations to perform:"))
    a=float(input("Enter your first number: "))
    b=float(input("Enter your second number: "))
    if choice==1:
        print(a, "+", b, "=" , ADD(a, b))
    elif choice==2:
        print(a, "-", b, "=", SUB(a, b))
    elif choice==3:
        print(a, "x", b,"=", MULT(a, b))
    elif choice==4:
        print(a, "/", b, "=", DIV(a, b))
    
#if the user want to continue the operations
    continue_operation=input("Do you want to continue?(yes/no): ")
    if continue_operation=="no":
        break
else:
    print("Invalid input")
