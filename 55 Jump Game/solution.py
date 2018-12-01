class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = 0
        for i in range(len(nums)):
            if i <= reach and nums[i] + i > reach:
                reach = nums[i] + i
            
        return reach >= len(nums) - 1
