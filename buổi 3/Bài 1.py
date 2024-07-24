import math
n=int(input("Mời bạn nhập số phần tửc của list N="))
L=[int(input()) for x in range(0,n)]
print("L=",L)
x=int(input("Mời bạn nhập một số bất kì :"))
k=L.count(x)
print("Số lần xuất hiện số",x,"trong list L là :",k)
L[2:8]=[8,5,4,0,1,3]
print("Sau khi thay thế ta được list là :")
print("L=",L)
Max=max(L)
Min=min(L)
print("Max=",Max)
print("Min=",Min)
Y=int(input("Mời bạn nhập một số bất kì Y="))
L.insert(0,Y)
print("L=",L)
if L == sorted(L) :
    print("Tăng")
elif L == sorted(L,reverse=True) :
    print("Giảm")
else :
    print("NO")
new_L=[sum(L[:i+1]) for i in range(n)]
print("new_L=",new_L)
'''
lst[:i+1]: Đây là cú pháp cắt (slicing) trong Python.
 Nó lấy một phần của danh sách lst từ phần tử đầu tiên (chỉ số 0) đến phần tử thứ i (bao gồm cả phần tử thứ i). 
 Ví dụ, nếu lst = [1, 2, 3, 4, 5] và i = 2, thì lst[:i+1] sẽ là [1, 2, 3].
'''
new2_L= [94, 39, 49, 6, -55, -37, 1, -23, -31, 1000]
print("new2_L=",new2_L)
print("Sắp xếp list mới theo giá trị tăng dần là new2_l=",sorted(new2_L))
new3_l=[int(math.fabs(new2_L[i])) for i in range(0,len(new2_L))]
print("new3_l=",new3_l)
print("Sau khi sắp xếp và theo giá trị thặng dư ta được các list mới sau :")
print("new3_l=",sorted(new3_l))