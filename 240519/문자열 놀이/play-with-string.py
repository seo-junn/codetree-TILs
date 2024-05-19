s,q = input().split()

for _ in range(int(q)):
    order = input().split()
    if order[0] == '1':
        temp = list(s)
        a,b = int(order[1])-1,int(order[2])-1
        temp[a], temp[b] = temp[b], temp[a]
        s = ''.join(temp)
    else:
        s = s.replace(order[1],order[2])
    print(s)