try:
    n1=int(input("Enter the 1st no: "))
    n2=int(input("Enter the 2nd no: "))
    c=n1/n2
    print("Div is", c) #if in n2 value we give zero we get zero div error
#except :
#    print("Div is not possible")
#or
except ZeroDivisionError: 
    print("Div is not possible")
except ValueError:
    print("Enter something ")