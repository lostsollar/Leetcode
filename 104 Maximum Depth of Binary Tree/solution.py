# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        My solution DFS
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return left + 1 if left > right else right + 1

    def maxDepth1(self, root):
        """
        BFS: My own solution
        reference: https://time.geekbang.org/course/detail/130-67635
        :param root: TreeNode
        :return: int
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
                    del queue[0]
        return level