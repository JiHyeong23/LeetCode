from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        x = 0
        nums = [x+1 for x in range(n)]
        return combinations(nums, k)