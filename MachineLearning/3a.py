numbers = [1,2,3,4,5,6]
print(numbers)
for i in numbers:
    
    print("Square: ", i*i)
    
print("\n")
for i in numbers:

    if i%2==0:
        print(i, "Even")
        print(" ")
    else:
        print(i, "odd")
        print(" ")


for i in numbers:
    if i>5:
        print(i)
