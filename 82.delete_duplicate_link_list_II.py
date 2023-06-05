# Definition for singly-linked list.
# 删除排序链表中的重复元素2
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-200)
        node = dummy
        cur = head

        pre = ListNode(-200)
        while cur != None:
            if cur.next != None:
                cur_next = cur.next
                if cur.val != cur_next.val and cur.val != pre.val:
                    temp = ListNode(cur.val)
                    node.next = temp
                    node = temp
            elif cur.val != pre.val:
                temp = ListNode(cur.val)
                node.next = temp
                node = temp
            pre = cur
            cur = cur.next
        return dummy.next