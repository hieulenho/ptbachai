
a = float(input("nhập a = "))
b = float(input("nhập b = "))
c = float(input("nhập c = "))


import math
delta = b**2 -4*a*c
if a == 0:
    if b == 0:
        if c == 0:
            print("pt vo so nghiem")
        else:
            print("pt vo nghiem")
    else:
        print('pt co nghiem duy nhat x = ', -c/b)
else:
    if delta > 0:
        x1 = (-b + math.sqrt(delta))/2*a
        x2 = (-b - math.sqrt(delta))/2*a
        print("phương trình có nghiệm là", x1,"và",x2)
    elif delta == 0:
        x3 = (-b/2*a)
        print("phương trình có nghiệm", x3)
    else:
        x = -b/(2*a)
        y1 = math.sqrt(4*a*c-b**2)/(4*(a**2))*2
        y2 = - math.sqrt(4*a*c-b**2)/(4*(a**2))*2
        x1 = complex(x,y1)
        x2 = complex(x,y2)
        print('pt có 2 nghiem la x1 = ' , x1 , 'và x2 = ' , x2)
    if a*c > 0:
        x5 = -b/(2*a)
        min = (x5**2)*a + b*x5 + c
        print('gia tri nho nhat cua ham so la MIN = ' , min , 'tai x = ' , x5)
    else:
        x4 = -b/(2*a)
        max = (x4**2)*a + b*x4 + c
        print('gia tri lon nhat cua ham so la MAX = ' , max , 'tai x = ' , x4)

    





