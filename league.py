for i in range(int(input())):
    x, y = input().strip().split()
    x, y = int(x), int(y)
    if (x % 3)  == (y % 3): print(x % 3)