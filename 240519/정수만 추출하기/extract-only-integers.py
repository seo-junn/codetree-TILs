a,b = input().split()
ans = 0
temp = ''
for c in a:
    if c.isdecimal(): temp += c
    else: break
ans += int(temp)

temp = ''
for c in b:
    if c.isdecimal(): temp += c
    else: break
ans += int(temp)

print(ans)