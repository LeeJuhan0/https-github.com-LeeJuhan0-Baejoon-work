import heapq

def solution(jobs):
    jobs.sort(key=lambda x: x[0])
    time = 0
    idx = 0
    heap = []
    total_time = 0
    while idx < len(jobs) or heap :
        while idx < len(jobs) and jobs[idx][0] <= time :
            heapq.heappush(heap, (jobs[idx][1], jobs[idx][0]))
            idx += 1
        if heap :
            cur_length, cur_start = heapq.heappop(heap)
            time += cur_length
            total_time += (time - cur_start)
        else : 
            time = jobs[idx][0]
    avg = total_time//len(jobs)
    return avg