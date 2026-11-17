"""WAP that accepts an integer and determines whether it is positive. negative, or zero. 
If it is positive, also state whether it is even or odd """
 
n=int(input("Enter a number:"))
if(n==0):
    print("Zero")
elif(n<0):
    print("Negative")
else:
    print("Positive")
    if(n%2==0):
        print("Even")
    else:
        print("Odd")