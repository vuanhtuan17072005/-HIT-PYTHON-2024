def check(num):
    try:
        int(num)
        return True
    except ValueError:
        return False
n=int(input("Mời bạn bạn nhập sô phần tử của mảng a:"))
mang_a=list(map(str,input().split()))
print(mang_a)
tuple_b=tuple(x for x in mang_a)
print("tuple_b là:")
print(tuple_b)
i=0
for num in tuple_b:
    if check(num):
        i+=1
print("Số phân tử có tất cả các chữ số trong tuple b là:",i)