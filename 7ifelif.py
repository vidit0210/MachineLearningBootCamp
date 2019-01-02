n1 = int(input("Enter Number 1"))
n2 = int(input("Enter Number 2:"))
n3  = int(input("Enter Number 3"))
if (n1 >n2 and n2>n3):
    print(n1," is Greater")
elif(n2>n1 and n2>n3):
    print(n2,"is Greater")
else:
    print(n3, "is Greater")