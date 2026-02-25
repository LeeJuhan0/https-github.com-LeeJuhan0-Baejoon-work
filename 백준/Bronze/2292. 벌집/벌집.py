n=int(input())

room = 1
i = 1
while True :
    if n <= i :
        break
    i += 6 * room
    room += 1
print(room)