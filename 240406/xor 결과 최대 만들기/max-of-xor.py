n, m = map(int,input().split())
nums = list(map(int,input().split()))

max_val = 0
def choose(curr_idx,num_cnt,val):
    if curr_idx == n:
        if num_cnt == m:
            global max_val
            max_val = max(max_val,val)
        return
    
    choose(curr_idx+1,num_cnt+1,val^nums[curr_idx])

    choose(curr_idx+1,num_cnt,val)

choose(0,0,0)
print(max_val)