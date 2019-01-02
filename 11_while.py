
password="QWERTY"
max_attempts = 3
attempt=0
while(attempt<max_attempts):
    your_pass = input("Enter Your pass")
    if(your_pass==password):
        print("Welcome")
        break
    attempt+=1
    print("Wrong Password Try again")



