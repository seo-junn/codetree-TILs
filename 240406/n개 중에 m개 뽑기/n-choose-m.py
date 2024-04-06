N, M = map(int,input().split())
comb = []

def find_comb(curr_num, cnt):
    if curr_num == N+1:
        if cnt == M:
            print(*comb)
        return
    
    comb.append(curr_num)
    find_comb(curr_num+1,cnt+1)
    comb.pop()

    find_comb(curr_num+1,cnt)

find_comb(1,0)