import random
import pprint
list1=["CNTT", "KHMT", "KTPM", "HTTT"]
choise=random.choice(list1)
D={
    "2023600001": choise+"2023600001",
    "2023600002": choise+"2023600002",
    "2023600003": choise+"2023600003",
    "2023600004": choise+"2023600004",
}
E={}
for i in range (4):
    M=f"Account{i+1}"
    for key,value in D.items():
       Username= key
       password=D[key]
       E[M]={
        "Username":Username,
        "password":password
        }
pprint.pprint(E)