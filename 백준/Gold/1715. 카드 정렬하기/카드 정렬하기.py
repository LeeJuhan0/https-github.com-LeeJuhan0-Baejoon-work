import sys
input = sys.stdin.readline
import heapq

n = int(input().strip())
cards = list(int(input().strip()) for _ in range(n))
heapq.heapify(cards)
answer = 0
while len(cards) > 1 :
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)
    answer += card1 + card2
    heapq.heappush(cards, card1 + card2)
print(answer)

    