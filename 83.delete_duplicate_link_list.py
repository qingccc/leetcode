# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        只用判断当前和上一个是否相同
        '''
        dummpy = ListNode(-200)
        node = dummpy

        cur = head
        pre = ListNode(-200)
        while(cur!=None):
            if cur.val != pre.val:
                tmp = ListNode(cur.val)
                node.next = tmp
                node = tmp
            pre = cur
            cur = cur.next
        return dummpy.next