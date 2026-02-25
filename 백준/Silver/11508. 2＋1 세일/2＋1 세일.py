n = int(input())
v = []
for i in range(n):
    v.append(int(input()))
v.sort()
price = []
sum = 0
while len(v) != 0:
    price.append(v.pop())
    if len(price) == 3:
        sum += price[0] + price[1]
        price = []

for i in price :
    sum += i
print(sum)