class Danger:
    def __init__(self,code='',color='',second=0):
        self.code = code
        self.color = color
        self.second = second

code,color,sec = input().split()
dang = Danger(code,color,int(sec))

print("code :",dang.code)
print("color :",dang.color)
print("second :",dang.second)