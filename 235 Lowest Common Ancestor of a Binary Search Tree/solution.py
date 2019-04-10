# —*- coding:utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        Solution is the same with 236
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left:
            return right
        elif not right:
            return left
        else:
            return root

    def lowestCommonAncestor1(self, root, p, q):
        """
        My solution
        如果 p、q 的值一个大于root的值，一个小于root的值，那么最近公共祖先一定是 root
        如果 p、q 的值同时小于或者大于 root 的值，那么左子树或者右子树递归调用该函数
        :param root:
        :param p:
        :param q:
        :return:
        """
        if p.val < root.val and q.val < root.val:
            ancestor = self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            ancestor = self.lowestCommonAncestor(root.right, p, q)
        else:
            ancestor = root
        return ancestor

    def lowestCommonAncestor2(self, root, p, q):
        """
        https://time.geekbang.org/course/detail/130-42708
        :param root:
        :param p:
        :param q:
        :return:
        """
        if p.val < root.val > q.val:
            return self.lowestCommonAncestor2(root.left, p, q)
        elif p.val > root.val < q.val:
            return self.lowestCommonAncestor2(root.right, p, q)
        return root


test = TreeNode(6)
test.left = TreeNode(2)

