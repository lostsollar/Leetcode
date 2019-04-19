# -*- coding:utf-8 -*-


class Solution(object):
    def lengthOfLIS0(self, nums):
        """
        DP
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = 1
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    # 因为dp[i]在每一轮循环中可能被赋值多次，因此要找最大的那个
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        return res

    @staticmethod
    def search(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if arr[mid] >= target:
                # 比如 arr 中只有一个元素，并且大于 target
                if mid - 1 < left or arr[mid-1] < target:
                    return mid
                right = mid - 1
            else:
                if mid + 1 <= right and arr[mid+1] >= target:
                    return mid + 1
                left = mid + 1
        return -1

    def lengthOfLIS(self, nums):
        """
        My own solution
        维护最长上升子序列
        :type nums: List[int]
        :rtype: int
        """
        res = []
        for i in range(len(nums)):
            index = self.search(res, nums[i])
            if index == -1:
                res.append(nums[i])
            else:
                res[index] = nums[i]
        return len(res)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
nums1 = [10, 11, 12, 13, 1, 2, 3, 4, 5]
checker = Solution()
print checker.lengthOfLIS(nums1)