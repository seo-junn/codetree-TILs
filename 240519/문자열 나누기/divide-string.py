n = int(input())
total = ''.join(input().split())

idx = 0
while idx < len(total):
    if idx+5 < len(total):
        print(total[idx:idx+5])
    else:
        print(total[idx:])
    idx += 5