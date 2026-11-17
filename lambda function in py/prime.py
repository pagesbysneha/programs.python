#WAP to check a num a prime or not
n=int(input("Enter a num: "))
prime=lambda n:n>1 and all (n%i!=0 for i in range (2,n))
print("prime" if prime(n) else "not prime")