n=int(input("Mời bạn nhập vào 1 số nguyên n="))
s=0
for i in range(1,n+1):
    if i%2==0:
        s-=i
    else :
        s+=i
print("S=",s)