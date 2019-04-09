# -*- coding:utf-8 -*-


class Solution(object):
    def canJump0(self, nums):
        """
        My solution

        :type nums: List[int]
        :rtype: bool
        """
        res = False
        cur_max = nums[0]
        for i in range(0, len(nums)):
            cur_max = max(cur_max, nums[i] + i)
            if cur_max >= len(nums) - 1:
                res = True
                break
            elif cur_max <= i:
                res = False
                break
        return res

    def canJump1(self, nums):
        """
        参考下面的 canJump 改进后的代码，简洁了一些，但是性能却不一定好
        因为上面原来的一旦判断可以跳出了，就跳出循环了
        :param nums:
        :return:
        """
        cur_max = 0
        for i in range(len(nums)):
            if cur_max >= i:
                cur_max = max(cur_max, nums[i] + i)
        return cur_max >= len(nums) - 1

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = 0
        for i in range(len(nums)):
            if i <= reach < nums[i] + i:
                reach = nums[i] + i
            
        return reach >= len(nums) - 1


test = [2, 3, 1, 1, 4]
test1 = [3, 2, 1, 0, 4]
test2 = [0]
checker = Solution()
print checker.canJump1(test1)












