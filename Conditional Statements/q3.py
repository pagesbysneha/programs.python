"""WAP program that accepts a student's marks (0-100) and 
displays the grade according to the following rules: 
90-100: 0, 80-89: E, 70-79. A, 60-69: B, 50-59 C, 40-49: D, 
and below 40: F Display an error message if the marks are outside the valid range"""

n=int(input("Enter the marks: "))
if(n<0 and n>100):
    print("Invalid marks")
if(n>=90 and n<=100):
    print("Grade O")
elif(n>=80 and n<=89):
    print("Grade E")
elif(n>=70 and n<=79):
    print("Grade A")
elif(n>=60 and n<=69):
    print("Grade B")
elif(n>=50 and n<=59):
    print("Grade C")
elif(n>=40 and n<=49):
    print("Grade D")
else:
    print("Grade F")