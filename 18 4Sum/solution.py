class Solution(object):
    def threeSum(self, nums, target):
        if len(nums) < 3:
            return []
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i - 1]:
                continue
            d = {}
            for x in nums[i + 1:]:
                if x not in d:
                    d[target-v-x] = 1
                else:
                    res.add((v, target-v-x, x))
        return map(list, res)

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-3]):
            if i > 0 and v == nums[i-1]:
                continue
            three_sums = self.threeSum(nums[i+1:], target-v)
            if three_sums:
                for one in three_sums:
                    one.insert(0, v)
                    res.add(tuple(one))
        return map(list, res)


checker = Solution()
nums = [1, 0, -1, 0, -2, 2]
target = 0
print checker.fourSum(nums, target)