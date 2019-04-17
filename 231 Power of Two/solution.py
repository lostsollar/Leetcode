class Solution(object):
    def isPowerOfTwo0(self, n):
        """
        My own solution
        :type n: int
        :rtype: bool
        """
        counter = 0
        if n > 0:
            while n:
                n = n & (n-1)
                counter += 1
        return counter == 1

    def isPowerOfTwo(self, n):
        """
        https://time.geekbang.org/course/detail/130-67647
        :type n: int
        :rtype: bool
        """
        return n and n & (n-1) == 0


n = 1
n1 = 16
n2 = 218
n3 = -16
n4 = 0
checker = Solution()
print checker.isPowerOfTwo(n)
print checker.isPowerOfTwo(n1)
print checker.isPowerOfTwo(n2)
print checker.isPowerOfTwo(n3)
print checker.isPowerOfTwo(n4)
