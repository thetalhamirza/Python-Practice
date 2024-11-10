def minOperations(x, y):

    if x < 2 * y:

        operations_x_increase = 2 * y - x
        operations_y_decrease = y - (x // 2) if y > (x // 2) else 100


    if y < 2 * x:

        operations_y_increase = 2 * y - x
        operations_x_decrease = x - (y // 2) if x > (y // 2) else 100

    minOps_x = min(operations_x_increase, operations_y_decrease)
    minOps_y = min(operations_y_increase, operations_x_decrease)

    return min(minOps_x, minOps_y)


for i in range(int(input())):
    x, y = map(int, input().split())

    if (x >= (y*2) or y >= (x*2)):
        print("0")
    else:
        print(minOperations(x, y))







### PREVIOUS INCORRECT SOLUTION


# def minOperations(x, y):

#     current = x
#     i = 0
#     flag = False
#     operations_x_down = 100
#     while current != 0 and not flag:
#         if (current*2) == y:
#             operations_x_down = i
#             flag = True
#         else:
#             i += 1
#             current -= 1 
    
#     i = 0
#     current = x
#     flag = False
#     operations_x_up = 100
#     while current <= 100 and not flag:
#         if current == (y*2):
#             operations_x_up = i
#             flag = True
#         else:
#             i += 1
#             current += 1

#     operations_x = min(operations_x_down, operations_x_up)

#     current = y
#     i = 0
#     flag = False
#     operations_y_down = 100
#     while current != 0 and not flag:
#         if (current*2) == x:
#             operations_y_down = i
#             flag = True
#         else:
#             i += 1
#             current -= 1

#     i = 0
#     current = y
#     operations_y_up = 100 
#     while current <= 100 and not flag:
#         if current == (x*2):
#             operations_y_up = i
#             flag = True
#         else:
#             i += 1
#             current += 1

#     operations_y = min(operations_y_down, operations_y_up)

#     return min(operations_x, operations_y)


