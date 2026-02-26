import math
from functools import reduce
def solution(arr):
    def lcm(a,b) :
        return abs(a*b)//math.gcd(a,b)
    answer = reduce(lcm, arr)
    return answer

