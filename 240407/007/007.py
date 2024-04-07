class zzs:
    def __init__(self, sc, mp, time):
        self.secret_code = sc
        self.meeting_point = mp
        self.time = time
    
    def __str__(self):
        return "secret code : " + str(self.secret_code) + "\nmeeting point : " + str(self.meeting_point) + "\ntime : " + str(self.time)
    
sc,mp,time = input().split()
z = zzs(sc,mp,int(time))
print(z)