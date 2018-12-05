class Solution(object):
    def wiggleMaxLength1(self, nums):
        """
        my own solution v1.0
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 2:
            return length
        result = 1
        last_diff = None
        for i in range(len(nums) - 1):
            cur_diff = nums[i+1] - nums[i]
            if cur_diff == 0:
                continue
            if last_diff and last_diff * cur_diff < 0:
                result += 1
            last_diff = cur_diff
        return result if result == 1 and not last_diff else result + 1
