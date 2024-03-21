import sys

line = sys.stdin.readline().strip()
alp = [0]*26

start = 0
end = 0

length = 0

while end < len(line):
    if alp[ord(line[end])-ord('a')]:
        length = max(length,end-start)
        while alp[ord(line[end])-ord('a')]:
            alp[ord(line[start])-ord('a')] -= 1
            start += 1
    else:
        alp[ord(line[end])-ord('a')] += 1
        end += 1

length = max(length,end-start)

print(length)