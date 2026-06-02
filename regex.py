import re
email = input("enter email : ")
if re.search(r"^.@.\.edu$",email):
    print("valid")
else:
    print("invalid")
