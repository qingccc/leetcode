'''
二叉树的右视图
'''
from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 每一层把最右侧的保存 层次遍历保存最右侧不为nullde值？
        '''
        1. 先获得树的高度
        '''
        queue = []
        queue.append(root)

        rs_list = []

        while queue or root != None:
            length = len(queue)
            for i in range(0, length):
                root = queue.popleft()
                rs_list.append(root.val)
                if root != None and not (root.left == None and root.right == None):
                    queue.append(root.left)
                    queue.append(root.right)
        return rs_list


