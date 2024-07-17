# Bài 1a
n=-1
tong =0
while n<=0:
    n=int(input("Mời bạn nhập một số nguyên dương n="))
while n>0 :
    so=n%10
    tong = tong + so
    n = n//10
print("Tổng các chữ số =",tong)
