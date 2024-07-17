a = float(input("Nhập giá trị của a: "))
b = float(input("Nhập giá trị của b: "))

# a cộng b
print("a + b =", a + b)

# a trừ b
print("a - b =", a - b)

# a nhân b
print("a * b =", a * b)

# a chia lấy nguyên b
print("a // b =", a // b)

# a mũ b
print("a ** b =", a ** b)

# a chia dư b
print("a % b =", a % b)

# So sánh a và b
if a > b:
    print("a lớn hơn b")
elif a < b:
    print("a nhỏ hơn b")
else:
    print("a bằng b")

# a AND b
print("a AND b =", a and b)

# a OR b
print("a OR b =", a or b)

# a XOR b
print("a XOR b =", a != b)

# NOT a == b
print("NOT a == b =", not (a == b))

# a dịch phải 1 đơn vị
print("a >> 1 =", int(a) >> 1)

# a dịch trái 1 đơn vị
print("a << 1 =", int(a) << 1)
