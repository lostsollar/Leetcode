class Solution(object):
    def majorityElement(self, nums):
        """
        My solution
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        res = {}
        for i in range(length):
            res[nums[i]] = res.get(nums[i], 0) + 1
            if res[nums[i]] * 2 > length:
                return nums[i]


checker = Solution()
test1 = [3, 2, 3]
test2 = [2, 2, 1, 1, 1, 2, 2]
print checker.majorityElement(test2)