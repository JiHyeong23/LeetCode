class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1,1,2]
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            for i in range(3,n+1):
                dp.append(dp[i-1]+dp[i-2])
        return dp[n]