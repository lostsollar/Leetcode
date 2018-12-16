# coding=utf-8


def climb_stairs(n):
    """
    DP [Accepted]
    Time Complexity: O(n)
    Space Complexity: O(1)
    :param n:
    :return res[n]:
    """
    if n < 3:
        return n
    one_step_before = 2
    two_step_before = 1
    res = 0
    for i in range(3, n+1):
        res = one_step_before + two_step_before
        two_step_before = one_step_before
        one_step_before = res

    return res


def climb_stairs1(n):
    """
    DP [Accepted]
    Time Complexity: O(n)
    Space Complexity: O(1)
    :param n:
    :return res[n]:
    对于x, y = y, x + y 是没有问题的， 因为 python 中会先把右侧的 x, x + y 先存起来
    然后同时对左侧的x, y 进行赋值
    """
    x, y = 1, 1
    for _ in range(1, n):
        x, y = y, x + y
    return y


print climb_stairs(0)
print climb_stairs(1)
print climb_stairs(2)
print climb_stairs(3)
