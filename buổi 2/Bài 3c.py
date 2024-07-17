import math

# Nhập các hệ số từ người dùng
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

# Tính delta
delta = b**2 - 4*a*c

if delta > 0:
    # Phương trình có hai nghiệm phân biệt
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}")
elif delta == 0:
    # Phương trình có nghiệm kép
    x = -b / (2*a)
    print(f"Phương trình có nghiệm kép: x = {x}")
else:
    # Phương trình không có nghiệm thực
    print("Phương trình không có nghiệm thực")