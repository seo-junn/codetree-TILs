class w_data:
    def __init__(self,date,day,weather):
        self.date = date
        self.day = day
        self.weather = weather
    
    def __str__(self):
        return self.date + ' ' + self.day + ' ' + self.weather

n = int(input())
datas = []
for _ in range(n):
    date,day,weather = input().split()
    datas.append(w_data(date,day,weather))

datas.sort(key=lambda x:x.date)

for i in range(n):
    if datas[i].weather == "Rain":
        print(datas[i])
        break