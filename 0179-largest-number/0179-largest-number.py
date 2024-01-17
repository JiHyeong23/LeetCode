class compare(str):
    def __lt__(a, b):
        return a+b > b+a

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        elif len(nums) == 0:
            return ""
        else: 
            lst = [str(x) for x in nums]
            sorted_lst = sorted(lst, key=compare)
            
            if list(set(sorted_lst)) == ['0']:
                sorted_lst = ['0']
                
        return ''.join(sorted_lst)
