import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(arr, start, end):
            idx = bisect.bisect_left(arr, target, start, end)
            if idx < len(arr) and arr[idx] == target:
                return idx
            else:
                return -1
        
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
                
        added = nums + nums[:left]
        ans = binary(added, left, len(added)-1)
        if ans == -1:
            return -1
        else:
            return ans % len(nums)