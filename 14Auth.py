id_pass ={'vidit0210':'qwerty','niraj':'asdfg'}

while True:
   print("Enter 1 to Register and Enter 2 to login")
   choice = int(input("Enter your Choice"))
   if(choice==2):
        username = input("Enter Username")
        password = input("Enter Password")
        if username in id_pass and password==id_pass[username]:
            print("Access Granted")
            break
        else:
            print("Denied")
   if(choice==1):
        username = input("Enter Username")
        password = input("Enter Password")
        id_pass[username]=password
        print('Registeration Complete')


