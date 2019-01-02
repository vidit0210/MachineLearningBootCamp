username=input("enter name:")
jee=int(input("enter mrks of jee:"))
hsc=int(input("enter mrks of hsc:"))
cet=int(input("enter mrks of cet:"))
if(jee>50 and hsc>75):
    print("candidate is eligible")
elif(cet>100 and hsc>75):
    print("candidate is eligible")
else:
    print("not eligible")