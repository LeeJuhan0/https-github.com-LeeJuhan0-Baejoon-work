n, m = map(int, input().split())
numbers = list(map(int, input().split()))
for _ in range(m):
    numbers.sort(reverse = True)
    card = numbers.pop() + numbers.pop()
    numbers.append(card)
    numbers.append(card)
print(sum(numbers))
