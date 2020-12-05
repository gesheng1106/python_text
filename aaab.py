dict1 = eval(input())
dict2 = eval(input())
temp = {}
temp.update(dict1)
temp.update(dict2)
for i in dict1.keys():
    if dict1.get(i) != temp.get(i):
        temp[i] = temp.get(i) + dict1.get(i)
ans = dict.fromkeys(sorted(temp))
for i in ans.keys():
    ans[i] = temp.get(i)
print(ans)
print(temp)