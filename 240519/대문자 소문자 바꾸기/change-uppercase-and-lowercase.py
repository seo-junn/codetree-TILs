ans = ''
for c in input():
    if c.isupper(): ans += c.lower()
    else: ans += c.upper()
print(ans)