# Nhập số n từ người dùng
n = int(input("Nhập số n: "))

print(f"Các số Armstrong bậc 3 từ 1 đến {n} là:")
for num in range(1, n + 1):
    # Chuyển số thành chuỗi để dễ xử lý từng chữ số
    num_str = str(num)
    # Lấy số chữ số của num
    num_digits = len(num_str)
    # Tính tổng lập phương các chữ số
    sum_of_cubes = sum(int(digit) ** 3 for digit in num_str)
    if sum_of_cubes == num:
        print(num)
