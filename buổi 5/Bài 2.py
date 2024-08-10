Q = input("Mời bạn nhập một chuỗi ký tự :")
charmax={}
for char in Q:
        if char in charmax:
            charmax[char]+=1
        else:
            charmax[char]=1
print("Số lần xuất hiện của các kỳ tự trong python là : ")
print(charmax)
