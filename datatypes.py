print(type("Hello"))

a=input ("Enter the statement")
print(type(a));
a=int(input ("Enter the statement"))
print(type(a));
a=float(input ("Enter the statement"))
print(type(a));

L=[1,2,3]
S1="Hello World"
print (S1[0:5])

if 'H' in S1:
    print("Found")
else: 
    print("Not found")

    
L=[1,2,54,12,80]
n=12
if n in L:
    print("found")
else: 
    print("Not found")

a,b,c=1,2,3
print(b)

S1="Hello,World"
print(S1.split(","))

print(len(S1))


# tp count the frequency
ns=' '
s="the world, the blue world!"
for i in s :
    if (i.isalnum() or i.isspace()) :
        ns=ns+i
print(ns)
l=ns.split(' ')
u=set(l)
for i in u:
    c=ns.count(i)
    print(i,"count:",c)


def fact(n):
    if (n<=1):
        return 1
    else:
        return n*fact(n-1)
print(fact(5))
