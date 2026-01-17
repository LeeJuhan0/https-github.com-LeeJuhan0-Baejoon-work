def solution(name):
    answer = 0
    n = len(name)
    for i in name:
        answer += min(ord(i) - ord('A'), ord('Z') - ord(i) + 1)
        
    move = n - 1
    for i in range(n):
        idx = i + 1
        while idx < n and name[idx] == 'A':
            idx += 1

        move = min(
            move,
            2 * i + (n - idx),
            i + 2 * (n - idx)
        )

    return answer + move
