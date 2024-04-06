import sys

n = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
base = sum(nums)

min_val = sys.maxsize
def choose(curr_idx,cnt,p_sum):
    if curr_idx == 2*n:
        if cnt == n:
            global min_val
            temp = base-p_sum
            min_val = min(min_val,abs(temp-p_sum))
        return
    
    choose(curr_idx+1,cnt+1,p_sum+nums[curr_idx])
    choose(curr_idx+1,cnt,p_sum)

choose(0,0,0)
print(min_val)