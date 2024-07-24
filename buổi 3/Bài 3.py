s1=input("Mời bạn nhập chuỗi s1 =")
s2=input("Mời bạn nhập chuỗi s2 =")
print("Đảo ngược của chuối s1 là :",s1[::-1])
a=int(input("Mời bạn nhập số a="))
b=int(input("Mời bạn nhập số b="))
print("Đảo ngược của chuỗi s2 trong 1<=a<b<=len(s2) là :")
if 1<=a and a<b and b<=len(s2):
    print(s2[:a]+s2[a:b][::-1]+s2[b:])
else:
    print("Bạn nhập số a,b sai yêu cầu chạy lai chương trình")
print("Xóa các vị trí chẵn trong s2 ta được 1 chuỗi là :",s2[1::2])
ss=""
for i in range(min(len(s1),len(s2))):
    ss=ss+s1[i]+s2[i]
print("Chuỗi đan sen của s1,s2 là :",ss)
'''
Trong đoạn mã trước đó, cụm min(len(s1), len(s2)) được sử dụng trong
 vòng lặp for để đảm bảo rằng vòng lặp chỉ chạy đến 
độ dài ngắn hơn của hai chuỗi
, tránh lỗi khi một chuỗi dài hơn chuỗi kia:
VD:
len(s1): Độ dài của s1 là 5.
len(s2): Độ dài của s2 là 6.
min(len(s1), len(s2)): Hàm min() sẽ trả về 5, vì 5 nhỏ hơn 6.
'''
print("Sau khi đổi kí tự đầu tiên của s1 và s2 ta được 1 chuỗi mới sau :")
print("new s1=",s1.replace(s1[0],s2[0]))
print("new s2=",s2.replace(s2[0],s1[0]))