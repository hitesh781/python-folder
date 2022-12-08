s=input()
res=""
for i in s*2:
    if i.isupper():
        res+=i
for i in s:
    if i.islower():
        res+=i
print(res)        


s