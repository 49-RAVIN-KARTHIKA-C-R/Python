n=int(input("Enter the number:"))
fact=1
i=1
while i<=n:
    fact=fact*i
    if i==n:
        print("Factorial of",n,"is",fact)
    i=i+1
