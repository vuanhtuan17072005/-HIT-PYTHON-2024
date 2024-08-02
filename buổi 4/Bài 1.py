tupe =("0","1","2","3","4","5","6","7","8","9")
tupe_number= tuple(int(x) for x in tupe)
print("tuple sau khi ép kiểu về số:")
print(tupe_number)
tong=0
for i in range(len(tupe_number)):
    tong  += tupe_number[i]
tongtb=float(tong/len(tupe_number))
print("Tổng trung bình các số trong tuple là: ",tongtb)