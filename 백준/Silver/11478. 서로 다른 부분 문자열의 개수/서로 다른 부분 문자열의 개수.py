word = str(input())
answer = []
for i in range(0,len(word)) :
    for j in range(i+1,len(word)+1):
        answer.append(word[i:j])
words = set(answer)
print(len(words))