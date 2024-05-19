line = input()

cnt1,cnt2 = 0,0
for i in range(len(line)-1):
    if line[i:i+2] == 'ee': cnt1 += 1
    elif line[i:i+2] == 'eb': cnt2 += 1
print(cnt1,cnt2)