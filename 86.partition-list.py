# Definition for singly-linked list.
'''
给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。

你应当 保留 两个分区中每个节点的初始相对位置。
'''
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        '''
        所有小于x的节点都移到第一个大于等于该节点值的节点之前
        '''
        dummy = ListNode(-200)
        dummy.next = head
        first_bigger_node = head
        cur = head
        index = 1
        first_pre = dummy
        cur_next = None
        cur_pre = dummy
        while cur != None:
            if cur.val >= x:
                first_bigger_node = cur
                break
            first_pre = cur

            cur = cur.next

        while cur != None:
            if cur.val < x:
                cur_next = cur.next
                cur_pre.next = cur_next
                first_pre.next = cur
                cur.next = first_bigger_node
                first_pre = cur
                cur = cur_next

            else:
                cur_pre = cur
                cur_next = cur.next
                cur = cur.next
        return dummy.next


