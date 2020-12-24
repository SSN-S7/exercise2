("Enter type of calculation need to be performed")
print("*For addition enter 1")
print("*For subtraction enter 2")
print("*For multiplication enter 3")
print("*For division enter 4")
print("*for any other input division will be performed by default")
print("x---------x-----------X-----------x")
a=int(input());
if a==1 :print
  print(" You have choosen addition")
  n1=int(input("enter number 1: "));
  n2=int(input("enter number 2:" ));
  sum=n1+n2;
  print("the sum of {0} and {1} is {2}".format(n1,n2,sum))
elif a==2 :
  print("You have choosen subtraction")
  n1=int(input("enter number 1: "));
  n2=int(input("enter number 2:" ));
  difference=n1+n2;
  print("the difference of {0} and {1} is {2}".format(n1,n2,difference))
elif a==3:
  print("You have choosen multiplication ")
  n1=int(input("enter number 1: "));
  n2=int(input("enter number 2:" ));
  product=n1*n2;
  print("the product of {0} and {1} is {2}".format(n1,n2,product))
else:
  print("You have choosen division")
  divident=int(input("enter divident : "));
  divisor=int(input("enter divisor:" ));
  answer=divident/divisor;
  print("the value after division of {0} and {1} is {2}".format(divident,divisor,answer))
