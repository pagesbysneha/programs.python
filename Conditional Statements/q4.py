"""WAP program that accepts a year and determines whether 
it is a leap year A leap year is divisible by 400, or 
it is divisible by 4 but not by 100"""

y=int(input("Enter the year: "))
if(y%100==0 and y%400==0) or (y%4==0 and y%100!=0):
    print("Leap year")
else:
    print("Not a leap year")