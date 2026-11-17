""" WAP that accepts three distinct numbers 
and displays the largest and the smallest number
using conditional statements."""

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))
"""if(a>b and a>c):
    print("Largest no. is", a) 
elif(b>a and b>c):
    print("Largest no. is", b)
else:
    print("Largest no. is", c)

if(a<b and a<c):
    print("Smallest no. is", a)
elif(b<a and b<c):
    print("Smallest no. is", b)
else:
    print("Smallest no. is", c)"""

if(a>b and a>c):
    large=a
elif(b>a and b>c):
    large=b
else:
    large=c

if(a<b and a<c):
    small=a
elif(b<a and b<c):
    small=b
else:
    small=c

print("Largest no. is:", large)
print("Smallest no. is:", small)