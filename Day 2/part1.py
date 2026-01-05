import math

file = open("/Users/prempatel/Desktop/INVENTYV/DAY 2/input.txt",'r')
dataInArray = file.readlines()

actualData = dataInArray[0]

splitedData = actualData.split(',')

invalid = []

invalidSum = 0

for i in splitedData:
    start = int(i.split('-')[0])
    end = int(i.split('-')[1])

    for j in range(start,end+1):
        isInvalid = True
        strData = str(j)
        start = 0
        end = len(strData)
        mid = math.floor((start + end)/2)
        while mid < end:
            if end % 2 != 0:
                break
            if strData[start] == strData[mid]:
                start = start + 1
                mid = mid + 1
            else:
                isInvalid = False
                break
        if isInvalid and end % 2 == 0:
            invalidSum = invalidSum + j
            invalid.append(j)

print(invalid)

print(invalidSum)


