d={}
str=input("enter")
for ch in str:
    if ch in d:
        d[ch]+=1
    else:
        d[ch]=1
for k in d:
        print(k,':',d[k])
print(dict(sorted(d.items(),key=lambda item: item[1],reverse=True)))
