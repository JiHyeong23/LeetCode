class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(list1, list2):
            re = []
            i = j = 0
            while i < len(list1) and j < len(list2):
                if list1[i] < list2[j]:
                    re.append(list1[i])
                    i += 1
                else:
                    re.append(list2[j])
                    j += 1
            
            while i < len(list1):
                re.append(list1[i])
                i += 1
            
            while j < len(list2):
                re.append(list2[j])
                j += 1
            
            return re
                    
        
        def merge_sort(lst):
            if len(lst) <= 1:
                return lst
            
            mid = len(lst) // 2
            L = lst[:mid]
            R = lst[mid:]
            
            L_sorted = merge_sort(L)
            R_sorted = merge_sort(R)
            
            return merge(L_sorted, R_sorted)
        
        return merge_sort(nums)