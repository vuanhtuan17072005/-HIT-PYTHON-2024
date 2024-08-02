def chisohanhphuc(arr,set_A,set_B):
    happted=0
    for char in arr:
        if char in set_A:
            happted+=1
        elif char in set_B:
            happted-=1
        else:
            continue;
    return happted
print("Mơi bạn nhập số nguyên n và m lần lượt là :")
n,m= map(int,input().split())
print("Mời bạn nhập mảng :")
arr = list(map(int,input().split()))
print("Mời bạn nhập các số yêu thích của mình (theo số lượng m):")
set_A= set(map(int,input().split()))
print("Mời bạn nhập các số mà bạn không yêu thích của mình (theo số lượng m):")
set_B= set(map(int,input().split()))
print("Tổng chỉ số hạnh phúc =",chisohanhphuc(arr,set_A,set_B))
