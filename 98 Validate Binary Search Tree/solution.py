# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # https://leetcode.com/problems/validate-binary-search-tree/submissions/
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        inorder = self.inorder(root)
        return inorder == list(sorted(set(inorder)))

    def inorder(self, root):
        if root is None:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

    # https://leetcode.com/problems/validate-binary-search-tree/submissions/
    def isValidBST1(self, root):
        self.prev = None
        return self.helper(root)

    def helper(self, root):
        if root is None:
            return True
        if not self.helper(root.left):
            return False
        if self.prev and self.prev.val >= root.val:
            return False
        self.prev = root
        return self.helper(root.right)


checker = Solution()
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
root1 = TreeNode(10)
root1.left = TreeNode(5)
root1.right = TreeNode(15)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(20)
print checker.isValidBST1(root)
