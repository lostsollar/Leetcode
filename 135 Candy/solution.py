def candy1(ratings):
    """
    Solution: Brute Force [Time Limit Exceeded]
    Time complexity: O(n2)
    Space complexity: O(n)
    :param ratings:
    :return:
    """
    length = len(ratings)
    candies = [1] * length
    flag = True
    while flag:
        flag = False
        for i in range(length):
            if i > 0 and ratings[i] > ratings[i-1] and candies[i] <= candies[i-1]:
                candies[i] = candies[i-1] + 1
                flag = True
            if i != length - 1 and ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
                candies[i] = candies[i+1] + 1
                flag = True
    return sum(candies)


def candy2(ratings):
    """
    Solution: Using Two Arrays [Accepted]
    Time complexity: O(n)
    Space complexity: O(n)
    :param ratings:
    :return:
    """
    length = len(ratings)
    left2right = [1] * length
    right2left = [1] * length
    for i in range(1, length):
        if ratings[i] > ratings[i-1]:
            left2right[i] = left2right[i-1] + 1
    for i in reversed(range(length-1)):
        if ratings[i] > ratings[i+1]:
            right2left[i] = right2left[i+1] + 1
    return sum(map(lambda x, y: x if x > y else y, left2right, right2left))


def candy3(ratings):
    """
    Solution: Using One Arrays [Accepted]
    Time complexity: O(n)
    Space complexity: O(n)
    :param ratings:
    :return:
    """
    length = len(ratings)
    candies = [1] * length
    for i in range(1, length):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1
    sum_candies = candies[length-1]
    for i in reversed(range(length-1)):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1]+1)
        sum_candies += candies[i]
    return sum_candies


def count(n):
    return n * (n+1) / 2


def candy4(ratings):
    """
    Solution: Single Pass Approach with Constant Space [Accepted]
    Time complexity: O(n)
    Space complexity: O(1)
    This solution is same with mine, but mine is bad
    :param ratings:
    :return:
    """
    length = len(ratings)
    if length < 2:
        return length

    candies = 0
    up = 0
    down = 0
    old_slope = 0
    for i in range(1, length):
        new_slope = 1 if ratings[i] > ratings[i-1] else (-1 if ratings[i] < ratings[i-1] else 0)
        if old_slope > 0 and new_slope == 0 or old_slope < 0 <= new_slope:
            candies += count(up) + count(down) + max(up, down)
            up = 0
            down = 0
        if new_slope > 0:
            up += 1
        if new_slope < 0:
            down += 1
        if new_slope == 0:
            candies += 1
        old_slope = new_slope
    candies += count(up) + count(down) + max(up, down) + 1
    return candies


def check_solution(func, test_set, index=None):
    if index is not None:
        print test_set[index]
        print func(test_set[index])
    else:
        for test in test_set:
            print test
            print func(test)


if __name__ == '__main__':
    test1 = [1, 1, 2, 3, 4, 2, 1, 1, 3, 5, 4, 3, 2, 1]
    test2 = [1, 1, 2, 3, 4, 2, 1, 1, 3, 5, 4, 3, 2, 1, 1]
    test3 = [1, 1, 2, 3, 4, 5, 2, 1, 1, 3, 5, 4, 3, 2, 1, 1, 1]
    test4 = [1, 1, 1, 1]
    test5 = [5, 4, 3, 2, 1, 1, 4]
    test6 = [5, 4, 3, 2, 1, 1, 4, 1]
    test7 = [1, 0, 2]
    test8 = [1, 2, 2]
    test9 = [2, 2, 1, 2, 2]
    test10 = [1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1]
    test11 = [4, 3, 3, 2, 1]
    test12 = [1, 2, 3, 4, 5, 3, 2, 1, 2, 6, 5, 4, 3, 3, 2, 1, 1, 3, 3, 3, 4, 2]
    tests = [test1, test2, test3, test4, test5, test6, test7, test8, test9, test10, test11, test12]

    check_solution(candy1, tests)
    check_solution(candy2, tests)
    check_solution(candy3, tests)
    check_solution(candy4, tests)




