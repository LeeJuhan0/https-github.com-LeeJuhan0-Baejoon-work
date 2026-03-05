word = input()
answer = ''
stack = []
store = False
for i in word:
    if i == '<' :
        store = True
        if stack :
            for j in range(len(stack)) :
                answer += stack.pop()
    elif i == ' ' :
        if stack :
            for j in range(len(stack)) :
                answer += stack.pop()
            answer += ' '
    if not store :
        if i != ' ':
            stack.append(i)
    else :
        answer += i
    if i == '>' :
        store = False

if stack :
    for j in range(len(stack)) :
        answer += stack.pop()
print(answer)