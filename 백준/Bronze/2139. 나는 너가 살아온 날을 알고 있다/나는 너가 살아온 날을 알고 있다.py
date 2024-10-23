def yunYears(years):
    yun = False
    if years % 4 == 0 and (years % 100 != 0 or years % 400 == 0): 
        yun = True
    return yun

def month(months, yun):
    cnt = 0 
    for i in range(1, 12, 1):
        if i == months: break

        if i == 2: 
            if yun == True: 
                cnt += 29
            else: cnt += 28

        if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
            cnt += 31
        elif i != 2:
            cnt += 30
    return cnt

# main
while True:
    Date = input().split()
    Date= [int(x) for x in Date]
    if Date[0] == 0 and Date[1] == 0 and Date[2] == 0:
        break

    ans = month(Date[1], yunYears(Date[2]))
    ans += Date[0]
    print(ans)
