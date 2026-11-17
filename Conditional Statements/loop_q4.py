#factorial of non negative integer
n=int(input("Enter the no. :"))
if(n>=0):
    f=1
    for i in range (1,n+1,1):
        f=f*i
    print("Factorial is ", f)
else:
    print("Enter positive no.")