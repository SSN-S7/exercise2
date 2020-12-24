# to obtain a character and convert to lowercase or uppercase
n=(input("enter a char"))
if ord(n)>=65 and ord(n)<=90 :
    print(chr((ord(n)+32)))
else:
    print(chr(ord(n)-32))

