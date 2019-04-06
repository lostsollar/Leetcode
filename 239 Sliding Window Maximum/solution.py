class Solution(object):
    """
    solution: deque(window save index instead of value)
    reference: https://time.geekbang.org/course/detail/130-41561
    """
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return nums
        window, res = [], []
        for i, x in enumerate(nums):
            if i >= k and window[0] <= i - k:
                window.pop(0)
            while window and nums[window[-1]] <= x:
                window.pop()
            window.append(i)
            if i >= k - 1:
                res.append(nums[window[0]])
        return res


nums = [1, 3, -1, -3, 5, 3, 6, 7]
nums1 = [1, 3, 1, 2, 0, 5]
checker = Solution()
test = checker.maxSlidingWindow(nums, 3)
print test
