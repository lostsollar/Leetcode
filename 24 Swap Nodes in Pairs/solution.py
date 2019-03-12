# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p_prev = None
        p_cur = head
        if p_cur is None or p_cur.next is None:
            return p_cur
        new_head = p_cur.next
        while p_cur and p_cur.next:
            p_next = p_cur.next
            if p_prev:
                p_prev.next = p_cur.next
            p_cur.next = p_next.next
            p_next.next = p_cur
            p_prev = p_cur
            p_cur = p_cur.next
        return new_head

    # https://time.geekbang.org/course/detail/130-41547
    def swapPairs2(self, head):
        # pre and pre.next have different type
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next


p_list = ListNode(1)
p_list.next = ListNode(2)
p_list.next.next = ListNode(3)
p_list.next.next.next = ListNode(4)
test = Solution()
#new_list = test.swapPairs1(p_list)
new_list1 = test.swapPairs2(p_list)
print "End"