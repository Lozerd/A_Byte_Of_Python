email = input()
count = 0
for i in email:
    count += 1
    if i == "@":
        print(email[count:])
