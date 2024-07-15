# -HIT-PYTHON-2024
# Python là ngôn ngữ thông dịch hay biên dịch?

Python thực tế là một ngôn ngữ thông dịch (interpreted language). Tuy nhiên, để hiểu rõ hơn, hãy xem xét các khía cạnh sau:

### Ngôn ngữ biên dịch (compiled language):
- Mã nguồn được dịch sang mã máy bởi trình biên dịch (compiler).
- Các ngôn ngữ như C, C++, Fortran, Java, Julia, Pascal thuộc nhóm này.
- Việc phát triển chương trình bằng ngôn ngữ biên dịch tốn thời gian hơn, nhưng sau khi mã nguồn đã được dịch, việc thực thi sau này nhanh hơn.

### Ngôn ngữ thông dịch (interpreted language):
- Mã nguồn được thực thi từng dòng lệnh ngay tức thời bởi trình thông dịch (interpreter).
- Python, MATLAB, R, JavaScript, PHP, GNU Octave, Mathematica thuộc nhóm này.
- Các ngôn ngữ thông dịch thường có một Interactive Prompt cho phép tương tác trực tiếp với máy tính.

Python thường được gọi là ngôn ngữ thông dịch vì mỗi lần chạy chương trình, mã nguồn được dịch lại. Tuy nhiên, nếu hiểu theo nghĩa rộng, không sai khi nói Python cũng là một ngôn ngữ biên dịch (compiled language). Khi thực thi, Python dịch mã nguồn thành bytecode, sau đó bytecode tiếp tục được thực thi bởi máy ảo (VM).

### Kiểu dữ liệu True, False trong Python:
Python sử dụng kiểu dữ liệu bool để biểu thị giá trị logic.
```python
sunny = True
rainy = False
