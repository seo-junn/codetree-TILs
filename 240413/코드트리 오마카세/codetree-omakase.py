import sys

L,Q = map(int,sys.stdin.readline().split())

guests = set()
sushi = {}
arrival_time = {}
position = {}

queries = []

for _ in range(Q):
    command = sys.stdin.readline().split()
    cmd = int(command[0])
    t,x,name,n = -1,-1,"",-1

    if cmd == 100:
        t,x = map(int,command[1:3])
        name = command[3]

        if name in sushi:
            sushi[name].append((t, x))
        else:
            sushi[name] = [(t, x)]

    elif cmd == 200:
        t,x = map(int,command[1:3])
        name = command[3]

        arrival_time[name] = t
        position[name] = x
        guests.add(name)

    else:
        t = int(command[1])

    queries.append((cmd,t,x,name,n))

for name in guests:
    px = position[name]
    p_in_time = arrival_time[name]
    p_exit_time = 0

    for su_time, sx in sushi[name]:
        if su_time < p_in_time:
            psx = (sx+(p_in_time-su_time))%L
            if psx <= px:
                time_diff = px-psx
            else:
                time_diff = px+L-psx
            eat_time = p_in_time + time_diff
        else:
            if sx <= px:
                time_diff = px-sx
            else:
                time_diff = px+L-sx
            eat_time = su_time + time_diff

        p_exit_time = max(p_exit_time,eat_time)

        queries.append((111,eat_time,-1,name,-1))

    queries.append((222,p_exit_time,-1,name,-1))

queries.sort(key=lambda x:(x[1],x[0]))

sushi = 0
people = 0
for q in queries:
    if q[0] == 100: sushi += 1
    elif q[0] == 111: sushi -= 1
    elif q[0] == 200: people += 1
    elif q[0] == 222: people -= 1
    else: print(people, sushi)