n = int(input())
lines = [tuple(map(int,input().split())) for _ in range(n)]
lines.sort()

cache_o = [-1]*n
cache_x = [-1]*n
def count_case(start,idx):
    if idx >= n:
        return 0
    res = 0
    if lines[idx][0] > start:
        if cache_o[idx] == -1: cache_o[idx] = count_case(lines[idx][1],idx+1)+1
        res = max(res,cache_o[idx])
    if cache_x[idx] == -1: cache_x[idx] = count_case(start,idx+1)
    res = max(res,cache_x[idx])
    return res
            
print(count_case(0,0))