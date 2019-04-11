class Solution(object):
    def myPow0(self, x, n):
        """
        My own solution
        Time Limit Exceeded
        :type x: float
        :type n: int
        :rtype: float
        """
        result = 1.0
        if n > 0:
            while n:
                result *= float(x)
                n -= 1
        elif n < 0:
            while n:
                result *= 1/float(x)
                n += 1
        return result

    def myPow(self, x, n):
        """
        Recursive
        https://time.geekbang.org/course/detail/130-42711
        :param x: float
        :param n: int
        :return: float
        """
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)

    def myPow1(self, x, n):
        """
        Not Recursive
        https://time.geekbang.org/course/detail/130-42711
        :param x: float
        :param n: int
        :return: float
        """
        if n < 0:
            x = 1/x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow


checker = Solution()
print checker.myPow(2, 2)
print checker.myPow(2, -2)
print checker.myPow(2, 0)
print checker.myPow(2.0, 10)
print checker.myPow(2.1, 3)
print checker.myPow(1.00001, 123456)
print checker.myPow(0.00001, 2147483647)
