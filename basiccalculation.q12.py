a=int(input("Enter the 1st side of triangle"))
b=int(input("Enter the 2nd side of triangle"))
c=int(input("Enter the 3rd side of triangle"))
if(a==b or b==c or a==c):
                         print("Isoceles triangle")
elif(a!=b and b!=c and a!=c):
                         print("Scalene triangle")
else:
                         print("Right angled triangle")
                         
