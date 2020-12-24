# to sove quadratic equation
# assume the equation to be ax^2 + bx +c
from math import sqrt
a=int(input("enter the coefficient of x^2"))
b=int(input("enter the coefficent of x"))
c=int(input("enter the constant"))
print(f"the roots of the equation are {(-b+(sqrt((b*b)-(4*a*c))))/(2*a)} and  {(-b-(sqrt((b*b)-(4*a*c))))/(2*a)}")
