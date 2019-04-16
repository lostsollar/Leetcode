class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        counter = 0
        while n:
            counter += 1
            n = n & (n-1)
        return counter


n = 00000000000000000000000000001011
n1 = 00000000000000000000000010000000
n2 = 000000000000000000000000
checker = Solution()
print checker.hammingWeight(n2)