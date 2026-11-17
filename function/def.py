def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b

a=int(input("Enter a no. : "))
b=int(input("Enter another no. : "))
print("Addition is", add(a,b))
print("Subtraction is", sub(a,b))
print("Multiplication is", mult(a,b))
if(b==0):
    print("Division if not possible")
else:
    print("Division is", div(a,b))