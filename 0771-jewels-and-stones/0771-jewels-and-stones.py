class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jws = list(jewels)
        answer = 0
        for i in range(len(jws)):
            answer += stones.count(jws[i])
        return answer