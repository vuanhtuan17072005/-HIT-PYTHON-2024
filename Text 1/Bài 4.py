a=list(map(str,input().split()))
a1=[]
for char in a:
    for i in range(0,len(char)):
        a1.append(char[i])
a1=set(a1)
print(a1)