class User:
    def __init__(self,ID='',level=0):
        self.ID = ID
        self.level = level
    
    def __str__(self):
        return 'user ' + self.ID + " lv " + str(self.level)

user1 = User('codetree',10)
user2 = User()
ID,lv = input().split()
user2.ID = ID
user2.level = int(lv)

print(user1)
print(user2)