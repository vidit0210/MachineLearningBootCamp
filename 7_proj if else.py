jio=float(input("enter no of bits of jio:"))
vod=float(input("enter no of bits of vod:"))
airtel=float(input("enter no of bits of airtel:"))
if(jio>vod and jio>airtel):
    print(jio,"is greater")
elif(vod>jio and vod>airtel):
    print(vod,"is greater")
else:
    print(airtel,"is greater")