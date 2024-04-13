import sys

table = {}
people = {}

def in_range(start,end,target):
    if end < L:
        if start < target <= end:
            return True
        else:
            return False
    else:
        if start < target <= end:
            return True
        else:
            start,end = 0,end%L
            if start <= target <= end:
                return True
            else:
                return False

def turn(time):
    global num_sushi
    new_table = {}
    if people:
        for key in table.keys():
            # extract table
            temp = table[key]
            for name in list(temp.keys()):
                if name not in people: continue
                if in_range(key,key+time,people[name][0]):
                    amount = min(temp[name],people[name][1])
                    temp[name] -= amount
                    people[name][1] -= amount
                    num_sushi -= amount
                    if temp[name] == 0: temp.pop(name)
                    if people[name][1] == 0: people.pop(name)

            if temp: new_table[(key+time)%L] = temp
    else:
        for key in table.keys():
            temp = table[key]
            new_key = (key+time)%L
            new_table[new_key] = temp
    return new_table

def put_sushi(x,name):
    global num_sushi
    num_sushi += 1
    if x in table:
        if name in table[x]:
            table[x][name] += 1
        else:
            table[x][name] = 1
    else:
        table[x] = {}
        table[x][name] = 1

L,Q = map(int,sys.stdin.readline().split())

present_time = 0
num_sushi = 0
for _ in range(Q):
    command = sys.stdin.readline().strip().split()
    table = turn(int(command[1])-present_time)
    present_time = int(command[1])
    if command[0] == '100':
        x,name = int(command[2]),command[3]
        if name in people and people[name][0] == x:
            people[name][1] -= 1
            if people[name][1] == 0:
                people.pop(name)
        else:
            put_sushi(x,name)

    elif command[0] == '200':
        x,name,n = int(command[2]),command[3],int(command[4])
        people[name] = [x,n]
        if x in table:
            if name in table[x]:
                amount = min(table[x][name],people[name][1])
                table[x][name] -= amount
                people[name][1] -= amount
                num_sushi -= amount
                if table[x][name] == 0: table[x].pop(name)
                if people[name][1] == 0: people.pop(name)

    else:
        print(len(people),num_sushi)