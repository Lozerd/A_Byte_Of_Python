email = str(input())
for i in range(1, len(email)):
    if "@" in email:
        print(email[i:])

# email = user@myserver.com
# count = 0
# for i in email:
#     count += 1
#     if (i == "@"):
#         print(email[count:])
