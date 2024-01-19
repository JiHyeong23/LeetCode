class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        if len(nums1) > len(nums2):
            for i in nums2:
                if i in nums1:
                    ans.append(i)
        elif len(nums1) < len(nums2):
            for i in nums1:
                if i in nums2:
                    ans.append(i)
        else:
            for i in nums1:
                if i in nums2:
                    ans.append(i)
        
        ans = list(set(ans))
        return ans