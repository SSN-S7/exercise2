# to check whether its a upper or lower or digit
n=input("enter the value to be tested")
if ord(n)>=65 and ord(n)<=90 :
    print(f"{n} is a uppercase letter")
elif ord(n)>=48 and ord(n)<=57 :
    print(f"{n} is a digit")
elif ord(n)>=97 and ord(n)<=122 :
    print(f"{n} is lowercase letter")
else :
    print(f"{n} is a symbol")

