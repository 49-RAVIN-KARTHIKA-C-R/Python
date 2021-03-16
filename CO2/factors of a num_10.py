n=int(input("Enter the number of terms:"))
factors=[]
for i in range(1,n):
    if n%i==0:
        factors.append(i)
factors.append(n)
print "factors of",n,"is",factors
