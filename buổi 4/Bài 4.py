def check(set_A,m):
    set_new =set()
    sorted_set_A=sorted(set_A)
    sum=0
    for num in sorted_set_A:
        if sum+num <= m :
           set_new.add(num)
           sum+=num
        else:
            break
    return set_new
n=int(input("Mời bạn nhập số phần tử của set n="))
set_A=set(map(int,input().split()))
print(set_A)
m=int(input("Mơi bạn nhập một số bất kì m="))
print(check(set_A,m))

