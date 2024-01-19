import bisect
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        
        ans = set()
        nums2.sort()
        for i in nums1:
            idx = bisect.bisect_left(nums2, i)
            if len(nums2) > idx and i == nums2[idx]:
                ans.add(i)
        return list(ans)
    
        '''ans = []
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
        '''