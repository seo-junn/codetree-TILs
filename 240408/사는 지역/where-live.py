class home:
    def __init__(self,name='',addr='',city=''):
        self.name = name
        self.addr = addr
        self.city = city
    
    def __str__(self):
        return "name " + self.name + "\naddr " + self.addr + "\ncity " + self.city

n = int(input())
homes = []
for _ in range(n):
    name, addr, city = input().split()
    homes.append(home(name,addr,city))

homes.sort(key=lambda x:x.name,reverse=True)
print(homes[0])