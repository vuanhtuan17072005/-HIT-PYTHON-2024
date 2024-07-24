
ho_va_ten =input("Mời bạn nhập họ và tên : ")
print(ho_va_ten.split())
# Hàm split là đữa 1 chuỗi về 1 dạng list các phần tử trong lish sẽ nganh cách nhau bởi 1 khoảng trắng
ho_va_ten = " ".join(ho_va_ten.split())
# Hàm join là nối các list với nhau thành 1 chuỗi
ho_va_ten_chuan=""
for tu in ho_va_ten.split():
    tu_chuan = tu[0].upper()+tu[1:].lower()
    ho_va_ten_chuan += tu_chuan + " "
ho_va_ten_chuan.strip()
print("Sau khi định dạng ta được họ và tên là :",ho_va_ten_chuan)
















