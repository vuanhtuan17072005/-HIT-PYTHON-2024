n = int(input("Nhập một số nguyên n="))
print(f"Số hoàn hảo từ 1 đến {n} là :")
for num in range(1,1+n):
    sum = 0
    for i in range(1,num):
        if num % i == 0:
          sum = sum+i
    if sum == num :
        print(num)
