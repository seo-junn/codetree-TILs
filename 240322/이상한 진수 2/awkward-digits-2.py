num = input().strip()

is_zero = False
for ch in num:
    if ch == '0':
        is_zero = True
        break

if is_zero:
    num = num.replace('0','1',1)
else:
    num = num[::-1].replace('1','0',1)[::-1]

print(int(num,2))