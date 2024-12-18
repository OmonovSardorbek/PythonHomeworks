list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
res=[]
for i in list1:
    if i not in list2:
        res.append(i)
for i in list2:
    if i not in list1:
        res.append(i)
print(res)