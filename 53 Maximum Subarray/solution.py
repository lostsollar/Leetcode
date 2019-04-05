# -*- coding:utf-8 -*-

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        当前方案每次都需要比较一次 cur_max
        实际上可以在 if 和 else 中分别加一句，可以减少比较次数，但是代码没有现在的简洁
        """
        cur_max = nums[0]
        cur_sum = nums[0]
        for i in range(1, len(nums)):
            if cur_sum >= 0:
                # if nums[i] < 0:
                #     cur_max = cur_max if cur_max >= cur_sum else cur_sum
                cur_sum += nums[i]
            else:
                cur_sum = nums[i]
                # cur_max = cur_max if cur_max >= cur_sum else cur_sum
            cur_max = cur_max if cur_max >= cur_sum else cur_sum

        return cur_max


checker = Solution()

test1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print checker.maxSubArray(test1)

test2 = [-100]
print checker.maxSubArray(test2)

test3 = [1]
print checker.maxSubArray(test3)

test3 = [-2, -1, -2]
print checker.maxSubArray(test3)