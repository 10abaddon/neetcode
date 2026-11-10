class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num={}
        for i in nums:
            if i in num:
                return True
            else:
                num[i]=1
        return False       