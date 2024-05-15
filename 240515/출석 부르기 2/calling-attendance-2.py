base = {1:"John",2:"Tom",3:"Paul",4:"Sam"}

while True:
    n = int(input())
    if n < 5: print(base[n])
    else:
        print("Vacancy")
        break