def count(string):
    base = set()
    for c in string:
        base.add(c)
    
    return len(base)

print("Yes" if count(input()) > 1 else "No")