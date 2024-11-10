days, reqTime = map(int, input().split())
sum = 0
maxPossible = 0
times = []
for i in range(days):
    minTime, maxTime = map(int, input().split())
    times.append({minTime, maxTime})
    maxPossible += maxTime
    
flag = False
while not flag:
    i = 0
    for element in times:
        sum += element[i]











if maxPossible < reqTime:
    print("NO")