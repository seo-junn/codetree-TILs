ans = ''
for c in input():
    if c.isdecimal(): ans += c
    if c.isalpha(): ans += c.lower()
print(ans)