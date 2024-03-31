def triangle(h,b):
    area=0.5*h*b 
    print("Area of triangle:",area)
def rectangle(l,w):
    afr=l*w
    print("Area of rectangle:",afr)
def circle(r):
    circ=3.14*r*r
    print("Area of circle:",circ)
def Square(s):
    Squar=s*s
    print("Area of Square:",Squar)
a=0
a=int(input('Enter 1 to find area of triangle\n2 for rectangle\n3 for circle\n4 for Square::'))
print(a)
if (a==1):
    print("You have choosen triangle!!!!!")
    h=int(input('Enter the value of Height:'))
    b=int(input('Enter the value of Breadth:'))
    triangle(h,b)
elif(a==2):
    print("You have choosen rectangle!!!!!")
    l=int(input('Enter the value of Length:'))
    w=int(input('Enter the value of width:'))
    rectangle(l,w)
elif(a==3):
    print("You have choosen Circle!!!!!")
    r=int(input('Enter the value of Radius:'))
    circle(r)
elif(a==4):
    print("You have choosen Square!!!!!")
    Squar=int(input('Enter the value of Sides:'))
    Square(Squar)
else:
    print("You have choosen wrong choose")


