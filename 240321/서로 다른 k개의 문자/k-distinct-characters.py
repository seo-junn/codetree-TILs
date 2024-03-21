import sys

line, k = sys.stdin.readline().split()
k = int(k)

start = 0
end = 0
alp = [0]*26
count = 0
length = 0

while end < len(line):
    if alp[ord(line[end])-ord('a')] == 0:
        count += 1
    alp[ord(line[end])-ord('a')] += 1

    if count > k:
        length = max(length,end-start)
        while count > k:
            alp[ord(line[start])-ord('a')] -= 1
            if alp[ord(line[start])-ord('a')] == 0:
                count -= 1
            start += 1
    
    end += 1

length = max(length,end-start)

print(length)