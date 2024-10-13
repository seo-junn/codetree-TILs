string = input().strip()
target = input().strip()

def find():
    l = len(target)
    for i in range(len(string)-l+1):
        if string[i:i+l] == target:
            return i
        
    return -1

print(find())