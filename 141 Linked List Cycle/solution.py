# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :my own solution
        :type head: ListNode
        :rtype: bool
        """
        p_slow = head
        if p_slow and p_slow.next:
            p_fast = p_slow.next
            while p_slow and p_fast:
                if p_slow == p_fast:
                    return True
                if p_fast.next is None:
                    return False
                p_fast = p_fast.next.next
                p_slow = p_slow.next
        return False

    def hasCycle1(selfs, head):
        """
        :https://time.geekbang.org/course/detail/130-41547
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False