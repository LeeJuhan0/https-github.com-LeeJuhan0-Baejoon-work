import heapq

def solution(operations):
    answer = []
    heap = []
    for i in operations :
        if i[0] == 'I' :
            heapq.heappush(heap,int(i[2:]))
        elif i[0] =='D' and heap :
            if i[2] != '-' :
                heap.remove(max(heap))
                heapq.heapify(heap)
            else :
                heapq.heappop(heap)

    if not heap:
        return [0, 0]
                

    return max(heap), min(heap)