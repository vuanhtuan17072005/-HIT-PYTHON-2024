import pprint
D = {
    "SV001":3.1,
    "SV002":3.6,
    "SV003":3.5,
    "SV004":3.4,
    "SV005":2.1,
    "SV006":1.8,
    "SV007":1.6,
}
i=0
for key,value in D.items():
    if D[key]>= 3.0 and D[key] <= 3.5:
        i+=1
print("Số sinh viên có tổng kết trong đoạn [3.0,3.5] là:",i)
print("Thêm 1 sinh viên mới vào từ điển ")
a=input("Mời bạn nhập mã sinh viên mới :")
b=float(input("Mời bạn nhập vào điểm GPA của sinh viên mới là :"))
if b<0:
    print("Điểm GPA không hợp lệ , điểm GPA không thể nào âm!")
else:
    D[a]=b
D.update(D)
newkey =[key for key,value in D.items() if value < 2.0 ]
for key in newkey:
    del(D[key])
print("Từ diển mới sau khi làm mới là:")
pprint.pprint(D)