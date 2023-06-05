# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        第一次相遇的时候  first比slow多走了nb 所以slow走了nb
        而从head走到slow a+nb  所以slow再走a步就可以走到相遇的地方

        根据：

        f=2s （快指针每次2步，路程刚好2倍）

        f = s + nb (相遇时，刚好多走了n圈）

        推出：s = nb

        从head结点走到入环点需要走 ： a + nb， 而slow已经走了nb，那么slow再走a步就是入环点了。

        如何知道slow刚好走了a步？ 从head开始，和slow指针一起走，相遇时刚好就是a步
        '''
        fast = head
        slow = head
        if head == None or head.next == None:
            return None
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        cur = head
        while cur != None and slow != None:
            if cur == slow:
                return cur
            cur = cur.next
            slow = slow.next
        return None
