ans = 0
temp = ''
for c in input():
    if c.isdecimal(): temp += c
ans += int(temp)

temp = ''
for c in input():
    if c.isdecimal(): temp += c
ans += int(temp)

print(ans)