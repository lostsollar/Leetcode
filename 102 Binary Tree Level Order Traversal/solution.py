# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        My solution
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root:
            queue = [root]
            while queue:
                cur = []
                counter = len(queue)
                for _ in range(counter):
                    cur.append(queue[0].val)
                    if queue[0].left:
                        queue.append(queue[0].left)
                    if queue[0].right:
                        queue.append(queue[0].right)
                    del queue[0]
                res.append(cur)
        return res