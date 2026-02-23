n = int(input())
words = [str(input()) for _ in range(n)]
d = {}
for word in words:
    try :
        d[word] += 1
    except :
        d[word] = 1
sorted(d, key = d.get)
max_len = -1
for i in d:
    if max_len < d[i] :
        max_len = d[i]
answer = []
for i in d:
    if d[i] == max_len:
        answer.append(i)
def quick(arr):
    if len(arr) <= 1 :
        return arr
    pivot = arr[0]
    return quick([x for x in arr[1:] if x < pivot]) + [pivot] + quick([x for x in arr[1:] if x >= pivot])
print(quick(answer)[0])

