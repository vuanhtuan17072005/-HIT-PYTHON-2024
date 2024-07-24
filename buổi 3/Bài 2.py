k=int(input("Mời bạn nhập số phần tử của list a là k="))
a=[int(input()) for x in range(k)]
L=[]
n=int(input("Mời bạn nhập số dòng n="))
m=int(input("Mời bạn nhập số cột m="))
if m*n >k :
    print("No")
else:
    for i in range(n):
        row=a[i*m:(i+1)*m]
        L.append(row)
print("L=",L)

