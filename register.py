users = {}
for i in range(int(input())):
    user = input()
    if user not in users:
        print("OK")
        users[user] = 1
    else:
        print(f"{user}{users[user]}")
        users[user] += 1






# ANOTHER FAILED SOLUTION : TIME LIMIT EXCEEDING

# users = []
# dups = []
# dupsCount = []
# dupPointer = 0
# for i in range(int(input())):
#     user = input()
#     if user not in users:
#         print("OK")
#         users.append(user)
#     else:
#         if user not in dups:
#             dups.append(user)
#             dupsCount.append(1)
#             dupPointer += 1
#             print(user + "1")
#         else:
#             for i in range(dupPointer):
#                 if dups[i] == user:
#                     break
#             dupsCount[i] += 1
#             print(user + str(dupsCount[i]))




# ANOTHER FAILED SOLUTION : TIME LIMIT EXCEEDING


# users = []
# for i in range(int(input())):
#     user = input()
#     if user not in users:
#         print("OK")
#         users.append(user)
#     else:
#         users.append(user)
#         count = -1
#         for element in users:
#             if element == user: count += 1
#         print(user + str(count))