n = int(input())
lengths = list(list(map(int, input().split())) for _ in range(6))
count = [0 for _ in range(5)]
for i in lengths:
    if i[0] == 1 :
        count[1] += 1
    if i[0] == 2 :
        count[2] += 1
    if i[0] == 3 :
        count[3] += 1
    if i[0] == 4 :
        count[4] += 1
big_square = 1
small_square = 1
for i in range(1,5) :
    if count[i] == 1:
        for j in range(len(lengths)):
            if i == lengths[j][0]:
                big_square *= lengths[j][1]
                small_square *= lengths[(j+3) % len(lengths)][1]

print((big_square-small_square)*n)