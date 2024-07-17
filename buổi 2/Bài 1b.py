n = -1
while n<0 :
    n = int(input("Mời bạn nhập vao một số nguyên dương n="))
else:
    tong = 0
    for i in range(1,n+1):
        if n % i == 0:
            tong = tong + i
print("Tổng các ước của số nguyên",n,"=",tong)

