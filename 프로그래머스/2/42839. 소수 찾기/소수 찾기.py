from itertools import permutations
def solution(numbers):
    answer = 0
    nums = set()
    no = set()
    for r in range(1, len(numbers)+1):
        for p in permutations(numbers, r):
            nums.add(int(''.join(p)))
    nums.discard(0)
    nums.discard(1)
    for i in nums:
        for j in range(2, int(i**0.5)+1):
            if i % j == 0 :
                no.add(i)
                break
    return len(nums) - len(no)