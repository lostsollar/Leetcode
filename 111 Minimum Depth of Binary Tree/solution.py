# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        My own solution: DFS
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if not left:
            return right + 1
        elif not right:
            return left + 1
        else:
            return left + 1 if left < right else right + 1

    def minDepth1(self, root):
        """
        My own solution: BFS
        Reference: https://time.geekbang.org/course/detail/130-67635
        :type root: TreeNode
        :rtype: int
        """
        level = 0
        if root:
            queue = [root]
            while queue:
                level += 1
                for _ in range(len(queue)):
                    if queue[0].left:
                        queue.append(queue[0].left)
                    if queue[0].right:
                        queue.append(queue[0].right)
                    if not (queue[0].left or queue[0].right):
                        queue = []
                        break
                    del queue[0]
        return level

    def minDepth2(self, root):
        """
        Reference: https://time.geekbang.org/course/detail/130-67635
        :param root:
        :return:
        """
        if root is None:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        return left + right + 1 if not left or not right else min(left, right) + 1





