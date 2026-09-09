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