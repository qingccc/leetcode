# Definition for singly-linked list.
'''
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

思路：
链表相加 最好新建一个表头
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        rs = ListNode()  # 返回的链表头
        p = rs
        carry = 0
        while (l1 is not None or l2 is not None):
            item1 = l1.val if l1 is not None else 0
            item2 = l2.val if l2 is not None else 0
            sum = item1 + item2 + carry
            # print(sum)
            curr = sum % 10
            carry = int(sum / 10)
            # print("carry",carry)
            p.next = ListNode(curr)
            p = p.next
            if (l1 is not None):
                l1 = l1.next
            if (l2 is not None):
                l2 = l2.next

        if (carry != 0):
            p.next = ListNode(carry)
        return rs.next

if __name__ == '__main__':
    so = Solution()
    print(so.addTwoNumbers())