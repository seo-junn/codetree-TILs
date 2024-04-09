import sys

n = int(sys.stdin.readline())
tower = [int(sys.stdin.readline()) for _ in range(n)]
s1,e1 = map(lambda x:int(x)-1,sys.stdin.readline().split())
s2,e2 = map(lambda x:int(x)-1,sys.stdin.readline().split())

tower = tower[:s1] + tower[e1+1:]
tower = tower[:s2] + tower[e2+1:]
print(len(tower))
for i in tower: print(i)