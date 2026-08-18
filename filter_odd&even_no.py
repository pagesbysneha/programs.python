#WAP To filter out even or odd no. from a list

num = [20, 4, 56, 11, 32, 14]
#even
def myfunc(x):
    if x % 2 == 0:
        return True
    else:
        return False

even = filter(myfunc, num)
print(list(even))
#odd
def myfunc_odd(x):
    if x % 2 != 0:  
        return True
    else:
        return False

odd = filter(myfunc_odd, num)
print(list(odd))
