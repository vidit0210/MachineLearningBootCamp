Nike ={
    "RunningShoes":{"Price":4056,"Size":{"8":1,"9":3,"10":5}},
    "Sneakers":{"Price":3000,"Size":{"9":5,"10":4}}
    }
Adidas ={
    "FootballShoes":{"Price":3600,"Size":{"10":3,"9":4}},
    "CricketShoes":{"Price":4000,"Size":{"8":2,"6":5}}
}
BrandsAvailable =["Nike","Adidas"]
def getDetails():
    kind = input("Enter Type of Shoes")
    footSize = input("Enter FootSize")
    return  kind,footSize

def getNikeSize():
    kind,Footlength = getDetails()
    return Nike[kind]["Size"][Footlength]

def getPrice(brand):
    kind,Footlength =getDetails()
    if(brand=="Nike"):
        return Nike[kind]["Price"]
    if(brand=="Adidas"):
        return Adidas[kind]["Price"]

totalbill=0
while True:
    user_brand = input("Which brand would you like to buy?")

    if(user_brand in BrandsAvailable):
        if(user_brand=="Nike"):
            size = getNikeSize()
            if(size<=0):
                print("Size not available")
            else:
                totalbill+=getPrice(user_brand)
                print("Adding into your shopping Cart..")
    ans = input("Would you like to Continue Shopping?")
    # else:
    #     print("Brand not Available!")
    #
    if(ans=="No"):
        break

print("Your Bils is :",totalbill)
coupons ={"50OFF":0.5,"20OFF":0.2}
apply_coupon = input("Enter Coupon")
if apply_coupon in coupons:
    discount = totalbill*coupons[apply_coupon]
    totalbill = totalbill-discount
    print("After Coupon your bill is:",totalbill)
else:
    print("Invalid Coupon")



