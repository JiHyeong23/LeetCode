class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_num = max(candies)
        answer = []
        for candy in candies:
            if candy + extraCandies >= max_num:
                answer.append(True)
            else:
                answer.append(False)
        return answer
