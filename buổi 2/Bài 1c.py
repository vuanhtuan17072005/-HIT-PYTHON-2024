a=-1
b=-1
c=-1
while a<0 or b<0 or c<0:
    a=int(input("Cạnh a ="))
    b=int(input("Cạnh b ="))
    c=int(input("Cạnh c ="))
else :
    if (a+b)>c and (a+c)>b and (a+c)>c:
        print("3 số nguyên dương trên tạo thành 1 tam giác :")
        if a**2+b**2==c**2 or a**2+c**2==b**2 or b**2 + c**2==a**2 :
            print("Là tam giác vuông")
        elif a==b and a==c:
            print("Là tam giác đều")
        elif a==b or b==c or c==a:
            print("Là tam giác cân")
        elif  a**2 + b**2< c**2 or a**2+ c**2< b**2 or b**2 + c**2 < a**2:
            print("Là tam giác tù")
        else:
            print("Là tam giác nhọn")








