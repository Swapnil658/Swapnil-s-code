a= int(input("Enter your 4 digit PIN:"))
if a<=9999 or a>=1000:
    print("PIN saved succesfully")
elif a>9999 or a<1000:
    print("Incorrect PIN")

name= input("Enter your Name:")
branch= input("Enter your Branch:")

b= int(input("Enter your IFSC Code:"))
if b<=9999 or b>=1000:
    print("Hello",name)
    print("WELCOME TO STATE BANK OF INDIA")
elif b>=9999 or b<=1000:
    print("Incorrect PIN")