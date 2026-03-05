word = input()
target = input()
m = len(word)
n = len(target)
idx = 0
answer = 0
for i in range(m-n+1):
    if i < idx :
        continue
    if word[i:i+n] == target :
        answer += 1
        idx = i + n - 1
    idx += 1

print(answer)