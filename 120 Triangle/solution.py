def minimum_total(triangle):
    """
    DP [Accepted]
    Time Complexity: O(n*m)
    Space Complexity: O(1)
    :param triangle:
    :return triangle[0][0]:
    """
    for i in reversed(range(len(triangle)-1)):
        for j in range(len(triangle[i])):
            triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]


def traverse(triangle, i, j):
    if i < len(triangle) and j < len(triangle[i]):
        if i == len(triangle) - 1:
            return triangle[i][j]
        return min(traverse(triangle, i+1, j), traverse(triangle, i+1, j+1)) + triangle[0][0]
    return 0


def minimum_total1(triangle):
    """
    Recursion Local is right, but on Leetcode is wrong
    Time Complexity: O(n)
    :param triangle:
    :return:
    """
    return (triangle[0][0] if len(triangle) == 1 else
            min(traverse(triangle, 0, 0), traverse(triangle, 0, 1)) + triangle[0][0])


if __name__ == "__main__":
    test1 = [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]
    print minimum_total(test1)
    print minimum_total1(test1)