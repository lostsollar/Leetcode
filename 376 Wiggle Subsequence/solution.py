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

    def wiggleMaxLength2(self, nums):
        """
        Linear Dynamic Programming [Accepted]
        Time complexity: O(n)
        Space complexity: O(n)
        """
        length = len(nums)
        if length < 2:
            return length
        up = [1]
        down = [1]
        for i in range(1, length):
            if nums[i] > nums[i-1]:
                up.append(down[i-1] + 1)
                down.append(down[i-1])
            elif nums[i] < nums[i-1]:
                up.append(up[i-1])
                down.append(up[i-1] + 1)
            else:
                up.append(up[i-1])
                down.append(down[i-1])
        return max(up[-1], down[-1])

    def wiggleMaxLength2(self, nums):
        """
        Linear Dynamic Programming [Accepted]
        Time complexity: O(n)
        Space complexity: O(1)
        """
        length = len(nums)
        if length < 2:
            return length
        up = 1
        down = 1
        for i in range(1, length):
            if nums[i] > nums[i-1]:
                up = down + 1
            elif nums[i] < nums[i-1]:
                down = up + 1
        return max(up, down)
