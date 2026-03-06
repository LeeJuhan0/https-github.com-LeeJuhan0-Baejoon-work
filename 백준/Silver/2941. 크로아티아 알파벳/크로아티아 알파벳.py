word = input()

target = ['c=','c-','d-','lj','nj','s=','z=']

for i in range(len(word)-2):
    if word[i:i+3] == 'dz=' :
        word = word[:i] + '*' + word[i+3:]

for i in range(len(word)-1):
    if word[i:i+2] in target :
        word = word[:i] + '*' + word[i+2:]
print(len(word))
        

