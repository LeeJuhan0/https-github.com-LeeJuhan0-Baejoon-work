n = int(input())

for _ in range(n) :
    m = int(input())
    d = {}
    for _ in range(m):
        v, k = input().split()
        try :
            d[k].add(v)
        except :
            d[k] = set()
            d[k].add(v)
    answer = []
    for key in d :
        answer.append(len(list(d[key]))+1)
    mul = 1
    for i in answer:
        mul *= i 
    
    print(mul-1)        