line = list(input())

c = ''
count = 0
ans = ''
for l in line:
    if l == c:
        count += 1
    else:
        ans += c + str(count)
        c = l
        count = 1
ans += c + str(count)
ans = ans[1:]
print(len(ans))
print(ans)