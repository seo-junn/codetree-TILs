base = ["apple","banana","grape","blueberry","orange"]

c = input()
ans = []

for item in base:
    if item[2] == c or item[3] == c: ans.append(item)

for item in ans: print(item)
print(len(ans))