dot = list(map(float, input().split()))
A, B, C = [dot[0]] + [dot[1]], [dot[2]] + [dot[3]], [dot[4]] + [dot[5]]
check = True
if (A[0] == B[0] and A[1] == B[1]) or (A[0] == C[0] and A[1] == C[1]) or (C[0] == B[0] and C[1] == B[1]):
    check = False
if (A[0] == B[0] and B[0] == C[0]) or (A[1] == B[1] and A[1] == C[1]) :
    check = False
try:    
    if (A[1] - B[1])/(A[0] - B[0]) ==  (A[1] - C[1])/(A[0] - C[0])  :
        check = False
except :
    pass
answer = []


square = ((A[0] - B[0])**2 + (A[1] - B[1])**2)**(0.5) + ((A[0] - C[0])**2 + (A[1] - C[1])**2)**(0.5)
answer.append(square*2)
square = ((A[0] - B[0])**2 + (A[1] - B[1])**2)**(0.5) + ((B[0] - C[0])**2 + (B[1] - C[1])**2)**(0.5)
answer.append(square*2)
square = ((A[0] - C[0])**2 + (A[1] - C[1])**2)**(0.5) + ((B[0] - C[0])**2 + (B[1] - C[1])**2)**(0.5)
answer.append(square*2)

print(max(answer)-min(answer) if check else -1)
