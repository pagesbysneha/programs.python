#Custom exception or user define exception
class InvalidAgeException(Exception):
    pass
try:
    age=int(input("Ennter your age: "))
    if (age<18):
            raise InvalidAgeException("Not eligible for vote")
    print("Ekigible for vote")
except InvalidAgeException as e:
    print ("Error is",e)