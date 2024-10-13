n, m = map(int,input().split())
base = list(map(int,input().split()))

def get_answer():
    global m
    answer = 0

    while m:
        answer += base[m-1]
        if m%2 == 0:
            m //= 2
        else:
            m -= 1
    
    return answer

print(get_answer())