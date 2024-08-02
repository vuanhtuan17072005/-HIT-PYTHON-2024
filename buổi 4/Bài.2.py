desk_A={"sv001","sv002","sv003"}
desk_B={"sv002","sv003","sv004"}
print("Sinh viên đăng kí ở bàn 1 là:",desk_A)
print("Sinh viên đăng kí ở bàn 2 là:",desk_B)
sv_dang_ky_chung= desk_A & desk_B
print("Số Sinh viên đăng ký cả hai bàn là ",sv_dang_ky_chung)
danhsachsvdangky=desk_A | desk_B
print("Danh sách số sinh viên đăng ký :",danhsachsvdangky)
danhsachloai1= desk_A - desk_B
print("Danh sách có ở bàn 1 mà không có ở bàn 2 là :",danhsachloai1)




