print("enter a value between 0 and 100 ")
marks=int(input("enter total marks of student"))
while marks>100 or marks<0 :
    marks=int(input("enter total marks of student"))
if marks>=90 :
    print("A grade")
elif marks>=75 :
    print("B grade")
elif marks>=50 :
    print("C grade")
else:
    print("fail")


