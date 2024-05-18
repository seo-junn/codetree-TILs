min_num = 101
min_count = 0

n = int(input())
for num in map(int,input().split()):
    if num < min_num:
        min_num = num
        min_count = 1
    elif num == min_num:
        min_count += 1

print(min_num,min_count)