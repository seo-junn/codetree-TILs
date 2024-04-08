import sys

students = []
N = int(sys.stdin.readline())

for i in range(1,N+1):
    h,w = map(int,sys.stdin.readline().split())
    students.append((h,w,i))

students.sort(key=lambda x:(-x[0],-x[1],x[2]))
for student in students: print(*student)