"""Write a menu-driven program that accepts two numbers and 
a choice of operation (addition, subtraction, multiplication, or division). 
Perform the selected operation using conditional statements, and 
handle division by zero and invalid choices appropriately."""

a=int(input("Enter 1st no. "))
b=int(input("Enter 2nd no. "))
c=input("Enter an operator ")
if(c=="+"):
    result=a+b
elif(c=="-"):
    result=a-b
elif(c=="*"):
    result=a*b
elif(c=="/"):
    if(b==0):
        print("Division is not possible")
    else:
        result=a/b
else:
    print("Invalid option")
print("Result is -> ", result)
