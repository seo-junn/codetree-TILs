n = int(input())
lines = [tuple(map(int,input().split())) for _ in range(n)]
lines.sort()

def count_case(start,idx):
    if idx >= n:
        return 0
    res = 0
    if lines[idx][0] > start:    
        res = max(res,count_case(lines[idx][1],idx+1)+1)
    res = max(res,count_case(start,idx+1))
    return res

print(count_case(0,0))