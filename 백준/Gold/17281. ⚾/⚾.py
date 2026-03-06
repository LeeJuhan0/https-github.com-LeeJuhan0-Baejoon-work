import sys
from itertools import permutations

input = sys.stdin.readline
 
def solve():
    N = int(input())
    enings = [
        (0,) + tuple(map(int, input().split()))
        for _ in range(N)
    ]  
 
    max_score = 0
 
    for permu in permutations(range(2, 10), 8):
        entry = permu[:3] + (1,) + permu[3:]
 
        hitter = 0
        score = 0
        for ening in enings:
 
            out = 0
            b1 = b2 = b3 = 0
 
            while out < 3:
                result = ening[entry[hitter]]
                hitter = (hitter + 1) % 9
 
                if result == 0:
                    out += 1
                elif result == 1:
                    score += b3
                    b1, b2, b3 = 1, b1, b2
                elif result == 2:
                    score += b2 + b3
                    b1, b2, b3 = 0, 1, b1
                elif result == 3:
                    score += b1 + b2 + b3
                    b1, b2, b3 = 0, 0, 1
                elif result == 4:
                    score += b1 + b2 + b3 + 1
                    b1 = b2 = b3 = 0
 
        max_score = max(max_score, score)
 
    print(max_score)
 
solve()