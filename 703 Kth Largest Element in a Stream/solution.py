import heapq


# Time Limit Exceeded
class KthLargest1(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.nums.append(val)
        return sorted(self.nums, reverse=True)[self.k - 1]


# Time Limit Exceeded
class KthLargest2(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = sorted(nums, reverse=True)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.nums) >= self.k:
            for i in range(self.k):
                if val >= self.nums[i]:
                    self.nums.insert(i, val)
                    break
        else:
            for i in range(self.k-1):
                if val >= self.nums[i]:
                    self.nums.insert(i, val)
                    break
            if len(self.nums) == self.k-1:
                self.nums.append(val)

        return self.nums[self.k-1]


# Min-Heap
# https://leetcode.com/problems/kth-largest-element-in-a-stream/discuss/148866/Python-simple-heapq-solution-beats-100
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        while len(self.pool) > k:
            heapq.heappop(self.pool)

    def add(self, val):
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


obj = KthLargest(3, [4, 5, 8, 2])
param_1 = obj.add(3)
param_2 = obj.add(5)
param_3 = obj.add(10)
param_4 = obj.add(9)
param_5 = obj.add(4)
print param_1
print param_2
print param_3
print param_4
print param_5
