# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head == None or head.next == None:
            return False
        fast = head  # 一次走2步
        slow = head  # 一次走一步
        while fast != None and slow != None and fast.next != None:
            if fast.next != None:
                fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False