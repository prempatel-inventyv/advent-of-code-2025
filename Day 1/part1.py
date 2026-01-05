file = open("/Users/prempatel/Desktop/INVENTYV/DAY 1/Day 1/text.txt",'r')

data = file.readlines() 

curr = 50

ans = 0

for i in data:
    side = i[0]
    number = int(i[1:])
    if side == 'L':
       curr = (curr - number) % 100
    elif side == 'R':
        curr = (curr + number) % 100
    if curr == 0:
        ans = ans + 1
    # print(i[0])
print(ans)