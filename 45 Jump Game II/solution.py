class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = 0
        curMax = 0
        curReach = 0
        for i in range(len(nums)):
            if curReach < i:
                jumps += 1
                curReach = curMax
            curMax = max(nums[i] + i, curMax)
        return jumps
