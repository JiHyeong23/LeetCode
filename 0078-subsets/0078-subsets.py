class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        
        def dfs(start, visited):
            answer.append(visited)
            for i in range(start, len(nums)):
                dfs(i+1, visited + [nums[i]])
                
        dfs(0, [])
        return answer