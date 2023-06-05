# leetcode

## 滑动窗口

滑动窗口主要用来处理连续问题。比如题目求解“连续子串 xxxx”，“连续子数组 xxxx”，就应该可以想到滑动窗口。能不能解决另说，但是这种敏感性还是要有的。

从类型上说主要有：

- 固定窗口大小
- 窗口大小不固定，求解最大的满足条件的窗口
- 窗口大小不固定，求解最小的满足条件的窗口（上面的 209 题就属于这种）

后面两种我们统称为`可变窗口`。当然不管是哪种类型基本的思路都是一样的，不一样的仅仅是代码细节。

**注意：**

记住最外层用for循环 不要用while循环

### 伪代码

```
初始化慢指针 = 0
初始化 ans

for 快指针 in 可迭代集合
   更新窗口内信息
   while 窗口内不符合题意
      扩展或者收缩窗口
      慢指针移动
   更新答案
返回 ans
```

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        滑动窗口
        '''
        max_len = 0
        win_map = {}
        win_left = 0 # 标记左端
        for index in range(len(s)):
            
            if s[index] in win_map:
                win_left = max(win_left,win_map.get(s[index])+1)      
            win_map[s[index]] = index
            max_len = max(max_len,index-win_left+1)
        return max_len

# 滑动窗口模板 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        滑动窗口
        '''
        max_len = 0
        win_left = 0
        win_right = 0
        used = set()
        while win_right < len(s):
            while s[win_right] in used:
                used.remove(s[win_left])
                win_left =win_left+1
            
            used.add(s[win_right])
            max_len = max(max_len,len(used))
            win_right +=1
            
        return max_len
```

注意：滑动窗口用map记录  key是字母 value是位置 后面应该也有value是次数的情况

不过上面这种set的形式更好理解 list不好操作

## 链表

如果链表中有用到cur.next = xxx,一定要注意判断cur.next 为空的情况 必要的时候需要加入if判断

即如果要使用cur.next 做赋值使用 或者要访问cur.next.next  一定要加上判断cur.next是否为空的条件

如果有可能修改头指针，最好定义一个新的头指针 dummy = listNode(0) 用一个不存在的实数初始化头

然后可以dummy.next = head  pre = dummy 返回的时候返回dummy.next 即可

快慢指针 如果要判断链表中是否有环 或者需要一个在另外一个特定步数前面做某项操作时，可以使用快慢指针 first= first.next.next  slow= slow.next

如果要判断环初始的位置 参考142题

画图判断目前是否有环

涉及到链表的拼接 使用穿针引线法

3个指针

pre now next

反转链表

next = cur.nex

.next = pre

cur = next

pre = cur

```python
# 链表遍历
node = LinkNode.head()
while node!=NULL:
  print(node.val)
  node = node.next
# 链表的新增在node的后面添加
tmp_node = LinkNode()
while node!=None:
    now = pre.next
    tmp_node.next = cur.next
    cur.next = tmp
    cur = tmp
# 反转链表   
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        pre = None
        while cur!=None:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre   
```

```python
# 合并两个有序链表
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1=list1
        cur2=list2
        index1=0
        index2 =0
        head = ListNode(1)
        if cur1==None:
            return cur2
        if cur2==None:
            return cur1
        cur = head
        while cur1!=None and cur2!=None:
            if cur1.val <= cur2.val:   
                cur.next = cur1      
                cur1 = cur1.next   
            else:
                cur.next = cur2
                cur2 = cur2.next  
            cur=cur.next  
        if cur1 == None:
            cur.next = cur2
        if cur2==None:
                cur.next = cur1
        return head.next

```

总结：

1. **使用替代指针** 见反转链接
   * 在反转的时候 需要有一个新指针先替代位置 防止找不到
   * tmp = cur.next cur.next = pre pre=cur cur=tmp
   * 最后返回pre即可
   * Pre 先用None代替
2. **虚拟头**  见合并两个有序链表
   * 虚拟头定义的时候 可以传入一个实参，否则是None，后面不能跟新节点 会报错
   * 返回的时候返回head.next 即可

**注意：**

不能成环

考虑边界值 不能为None

## 数组

## 树

## 回溯

## 动态规划