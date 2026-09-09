n=int(input("Enter the no: "))
sumofeven=0
for i in range(1,n+1):
    if(i%2==0):
        sumofeven=sumofeven+i
print("Sum is ", sumofeven)