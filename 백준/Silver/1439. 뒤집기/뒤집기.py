word = str(input())
flip = 0
for i in range(len(word)-1):
    if word[i] != word[i+1] :
        flip += 1
        
print(int((flip+1) // 2))