# -HIT-PYTHON-2024
Python là ngôn ngữ thông dịch hay biên dịch? Python thực tế là một ngôn ngữ thông dịch (interpreted language). Tuy nhiên, để hiểu rõ hơn, hãy xem xét các khía cạnh sau:
1.	Ngôn ngữ biên dịch (compiled language):
o	Mã nguồn được dịch sang mã máy bởi trình biên dịch (compiler).
o	Các ngôn ngữ như C, C++, Fortran, Java, Julia, Pascal thuộc nhóm này.
o	Việc phát triển chương trình bằng ngôn ngữ biên dịch tốn thời gian hơn, nhưng sau khi mã nguồn đã được dịch, việc thực thi sau này nhanh hơn.
2.	Ngôn ngữ thông dịch (interpreted language):
o	Mã nguồn được thực thi từng dòng lệnh ngay tức thời bởi trình thông dịch (interpreter).
o	Python, MATLAB, R, JavaScript, PHP, GNU Octave, Mathematica thuộc nhóm này.
o	Các ngôn ngữ thông dịch thường có một Interactive Prompt cho phép tương tác trực tiếp với máy tính.
Python thường được gọi là ngôn ngữ thông dịch vì mỗi lần chạy chương trình, mã nguồn được dịch lại. Tuy nhiên, nếu hiểu theo nghĩa rộng, không sai khi nói Python cũng là một ngôn ngữ biên dịch (compiled language). Khi thực thi, Python dịch mã nguồn thành bytecode, sau đó bytecode tiếp tục được thực thi bởi máy ảo (VM).
Kiểu dữ liệu True, False trong Python:
•	Python sử dụng kiểu dữ liệu bool để biểu thị giá trị logic.
•	True đại diện cho sự thỏa mãn của một điều kiện, còn False đại diện cho sự không thỏa mãn.
•	Ví dụ:
Python
sunny = True
rainy = False
Các kiểu dữ liệu trong Python: Python hỗ trợ nhiều kiểu dữ liệu tích hợp sẵn theo mặc định. Dưới đây là một số kiểu dữ liệu cơ bản:
1.	Kiểu dữ liệu chuỗi (String):
o	Được bao quanh bởi dấu ngoặc kép hoặc dấu nháy đơn.
o	Ví dụ: name = "John"
2.	Kiểu dữ liệu số (Numeric Types):
o	int: Số nguyên, dương hoặc âm, không có số thập phân.
o	float: Số thực, chứa số thập phân.
o	complex: Số phức.
o	Ví dụ: age = 22, point = 8.9
3.	Kiểu dữ liệu danh sách (List):
o	Là một tập hợp các phần tử có thứ tự, có thể thay đổi.
o	Ví dụ: option = [1, 2, 3, 4, 5]
4.	Kiểu dữ liệu tuple:
o	Tương tự danh sách, nhưng không thể thay đổi sau khi khởi tạo.
o	Ví dụ: info = ('John', 22, True)
5.	Kiểu dữ liệu từ điển (Dictionary):
o	Lưu trữ các cặp khóa-giá trị.
o	Ví dụ: person = {"name": "John", "age": 22, "male": True}
6.	Kiểu dữ liệu boolean (Bool):
o	Chỉ có hai giá trị: True (đúng) và False (sai).
o	Ví dụ: sunny = True, rainy = False
Mệnh đề điều kiện và vòng lặp:
•	Python hỗ trợ các mệnh đề điều kiện (if, elif, else) để kiểm tra điều kiện và thực hiện các hành động tương ứng.
•	Vòng lặp while thực hiện một khối mã nhiều lần dựa trên điều kiện kiểm tra.
•	Ví dụ về vòng lặp while:
Python
n = 0
while n < 5:
    n += 1
    print(n)
