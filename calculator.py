def calculator(a,b):
    x=a+b
    y=a-b
    z=a*b
    p=a/b
    return x,y,z,p
x=int(input("Enter a no.: "))
y=int(input("Enter another no.: "))
p,q,r,s=calculator(x,y)
print("Addition is ",p)
print("Subtraction is ",q)
print("Multiplication is ", r)
print("Division is ", s)
