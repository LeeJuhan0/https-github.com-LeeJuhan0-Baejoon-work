n = int(input())
string = [str(input()) for _ in range(n)]
s = set(string)
string = list(s)
string.sort(key = lambda x :(len(x), x))
for i in string:
    print(i)