str=input()
m=['a','e','i','u','o']
res=""
i=0
k=0
while i<len(str):
    k+=1
    res+=str[i] 
    if str[i] not in m  and k>=3 and i!=len(str)-1:
        res+="_"
        m.append(str[i])
        k=0
    i+=1
print(res)
