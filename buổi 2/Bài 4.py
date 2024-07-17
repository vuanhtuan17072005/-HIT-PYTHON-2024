n=int(input("Nhập số n cần tìm :"))
vt0 = 0
vt1 = 1
my_Fibonacci =[vt0,vt1]
for i in range(2,n):
    tong = vt0 + vt1
    my_Fibonacci.append(tong)
    vt0 = vt1
    vt1 = tong
print("Dãy số độ dài",n,f"bạn cần tìm là : {my_Fibonacci}")