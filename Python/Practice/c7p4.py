n = int(input("Enter a number: "))

for i in range(2,n):
    if(n%i)==0:
        print("not a prime number")
else:
    print("prime")
    