n, m = map(int,input().split())
nums = list(map(int,input().split()))

max_val = 0
chosen = []
def choose(curr_idx,num_cnt):
    if curr_idx == n:
        if num_cnt == m:
            global max_val
            temp = chosen[0]
            for i in range(1,m):
                temp ^= chosen[i]
            max_val = max(max_val,temp)
        return
    chosen.append(nums[curr_idx])
    choose(curr_idx+1,num_cnt+1)
    chosen.pop()

    choose(curr_idx+1,num_cnt)

choose(0,0)
print(max_val)