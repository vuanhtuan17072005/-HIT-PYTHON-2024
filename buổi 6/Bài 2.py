def matranchuyenvi(a):
    return [list(b) for b in zip(*a)]
def matran( m: int , n : int ) -> int:
    print("Mời bạn nhập giá trị cho từng phần tử trong mảng a:")
    a=[]
    for i in range(m):
        b=[]
        for j in range(n):
            nhap=int(input(f"Mời bạn nhập giá trị cho từng phần tử ở dòng ({i+1}) ở hàng thứ ({j+1}) là : "))
            b.append(nhap)
        a.append(b)
    return a
m=int(input("Mời bạn nhập số dong m="))
n=int(input("Mời bạn nhập số cột n="))
newa= matran(m,n)
print("Ma trận a của bạn sau khi nhập là :")
for a in newa:
    print(a)
print("Ma trận chuyển vị của ma trận a là :")
new=matranchuyenvi(newa)
for b in new:
    print(b)
