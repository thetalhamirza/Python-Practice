for i in range(int(input())):
    num, maxCal = input().strip().split()
    num, maxCal = int(num), int(maxCal)
    string = input().strip().split()

    sum = 0
    count = 0
    for element in string:
        if (sum + int(element)) <= maxCal: 
            sum += int(element)
            count += 1
        else:
            break            
    print(count)