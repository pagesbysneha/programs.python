try:
    n1=int(input("Enter the 1st no: "))
    n2=int(input("Enter the 2nd no: "))
    c=n1/n2
except ZeroDivisionError: 
    print("Div is not possible")
except ValueError:
    print("Enter something ")
else:
    print("Result is",c)
finally:
    print("Thank you ")