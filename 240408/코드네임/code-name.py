class Agent:
    def __init__(self,code_name='',score=0):
        self.code_name = code_name
        self.score = score
    
    def __str__(self):
        return self.code_name + ' ' + str(self.score)

agents = []
for _ in range(5):
    code,score = input().split()
    agents.append(Agent(code,int(score)))

agents.sort(key=lambda x:x.score)
print(agents[0])