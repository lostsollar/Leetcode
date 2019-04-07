# -*- coding:utf-8 -*-


# My solution [增加去重后，不超时了]
class Solution(object):
    def twoSum(self, nums, target):
        """
        one-pass hash table

        Parameters
        ----------
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        nums_dict = {}
        for i, x in enumerate(nums):
            if target - x in nums_dict:
                result.append([target - x, x])
            nums_dict[x] = i
        return result

    def threeSum1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = set()
        for i, x in enumerate(nums):
            if i >= 1 and x == nums[i-1]:
                continue
            two_sums = self.twoSum(nums[i+1:], -x)
            if two_sums:
                for one in two_sums:
                    one.insert(0, x)
                    result.add(tuple(one))
        return map(list, result)

    # https://time.geekbang.org/course/detail/130-42705
    # using map
    def threeSum2(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i-1]:
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, -v-x, x))
        return map(list, res)

    # https://time.geekbang.org/course/detail/130-42705
    # From both sides to the middle
    def threeSum3(self, nums):
        res = []
        nums.sort()
        for i in xrange(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return map(list, res)


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    nums1 = [-1, -1, -1, -1, 0, 1]
    checker = Solution()
    print checker.threeSum3(nums)