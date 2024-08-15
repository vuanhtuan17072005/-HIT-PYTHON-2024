def Tinhtong(n:int) -> int :
    Sum=0
    a = [int(i) for i in str(n)]
    for i in a:
        Sum+=i
    return Sum
n=int(input("Mời bạn nhập một số nguyên dương n="))
while n<=0:
    n = int(input("Mời bạn nhập lại n="))
print("Chúc mừng bạn đã nhập thành công ",n)
t=0
Sum=Tinhtong(n)
while True:
    t=t+1
    if Sum >=10:
        Sum=Tinhtong(Sum)
    else:
        break
print("Số lần cộng là :",t)
print("Số cuối cùng là :",Sum)

