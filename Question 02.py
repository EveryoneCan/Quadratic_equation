#import complex math module

import cmath

a=int(input("Enter the coefficient of x2 :"))
b=int(input("Enter the coefficient of x  :"))
c=int(input("Enter the constant value    :"))

#Calculate the discriminant
discrimi=(b**2)-(4*a*c)

#Find two solutions
x=(-b-cmath.sqrt(discrimi))/(2*a)
y=(-b+cmath.sqrt(discrimi))/(2*a)

#Give the output
if(discrimi>0):
    print("The discriminant is greater than zero -> There are two real distinct roots")
    print(f"The roots of,{a}x^2+{b}x+{c}=0,are: " ,end="")
    print("The solutaion are{0}and{1}".format(x,y))

if(discrimi==0):
    print("The discriminant is zero -> There are two real identical roots")
    print(f"The roots of,{a}x^2+{b}x+{c}=0,are: " ,end="")
    print("The solutaion are{0}and{1}".format(x,y))

if(discrimi<0):
   print("The discriminant is less than zero -> There are no real roots")    
