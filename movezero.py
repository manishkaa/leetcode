class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i1=0
        for i in nums:
            if i !=0:
                nums[i1]=i
                i1+=1
        while i1<len(nums):
            nums[i1]=0
            i1+=1
