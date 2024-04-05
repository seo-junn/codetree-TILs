import sys
from itertools import combinations

N, M, C = map(int,sys.stdin.readline().split())
room = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

max_score = 0

def taken(items,C):
    if sum(items) <= C:
        res = 0
        for i in items: res += i**2
        return res
    else:
        res = 0
        for l in range(len(items)):
            for item in combinations(items,l):
                if sum(item) <= C:
                    temp = 0
                    for i in item: temp += i**2
                    res = max(res,temp)
        return res

for row1 in range(N):
    for col1 in range(N-M+1):
        score1 = taken(room[row1][col1:col1+M],C)
        row2 = row1
        for col2  in range(col1+M,N-M+1):
            score2 = taken(room[row2][col2:col2+M],C)
            max_score = max(max_score,score1+score2)
        for row2 in range(row1+1,N):
            for col2 in range(N-M+1):
                score2 = taken(room[row2][col2:col2+M],C)
                max_score = max(max_score,score1+score2)

print(max_score)