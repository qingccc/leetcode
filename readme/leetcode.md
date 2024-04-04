# leetcode

## 滑动窗口

滑动窗口主要用来处理连续问题。比如题目求解“连续子串 xxxx”，“连续子数组 xxxx”，就应该可以想到滑动窗口。能不能解决另说，但是这种敏感性还是要有的。

从类型上说主要有：

- 固定窗口大小
- 窗口大小不固定，求解最大的满足条件的窗口
- 窗口大小不固定，求解最小的满足条件的窗口（上面的 209 题就属于这种）

后面两种我们统称为`可变窗口`。当然不管是哪种类型基本的思路都是一样的，不一样的仅仅是代码细节。

### [固定窗口大小](https://github.com/azl397985856/leetcode/blob/master/thinkings/slide-window.md#固定窗口大小)

对于固定窗口，我们只需要固定初始化左右指针 l 和 r，分别表示的窗口的左右顶点，并且保证：

1. l 初始化为 0
2. 初始化 r，使得 r - l + 1 等于窗口大小
3. 同时移动 l 和 r
4. 判断窗口内的连续元素是否满足题目限定的条件
   - 4.1 如果满足，再判断是否需要更新最优解，如果需要则更新最优解
   - 4.2 如果不满足，则继续。

### [可变窗口大小](https://github.com/azl397985856/leetcode/blob/master/thinkings/slide-window.md#可变窗口大小)

对于可变窗口，我们同样固定初始化左右指针 l 和 r，分别表示的窗口的左右顶点。后面有所不同，我们需要保证：

1. l 和 r 都初始化为 0
2. r 指针移动一步
3. 判断窗口内的连续元素是否满足题目限定的条件
   - 3.1 如果满足，再判断是否需要更新最优解，如果需要则更新最优解。并尝试通过移动 l 指针缩小窗口大小。循环执行 3.1
   - 3.2 如果不满足，则继续。

形象地来看的话，就是 r 指针不停向右移动，l 指针仅仅在窗口满足条件之后才会移动，起到窗口收缩的效果。

#### **注意：**

==记住最外层用for循环 不要用while循环==

#### 伪代码

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

next = cur.next

cur.next = pre

cur = next

pre = cur

```python
# 链表遍历
node = LinkNode.head()
while node!=NULL:
  print(node.val)
  node = node.next
# 链表的新增在node的后面添加 tenp是要加入的
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



**需要注意的问题**

1. 严谨度判断 一般是判断是都是null 如果是null 返回null
2. 对于while 循环里 一般是使用node !=null 表示遍历到最终节点 并且一般我们在循环体里会使用 node.next
   如果这里使用node.next!=null 那么终止条件是 node.next==null node 对应的是最后一个有值的节点 一般是因为我们要去去这些的值
   ![image-20230910164506347](leetcode.assets/image-20230910164506347.png)

如果非此种情况，而是正常的遍历 那么使用的话就需要返回node.next 感觉比较麻烦

**总之，正常情况下 使用while(node != null )的这种情况多一点**

## 数组

## 树



## 回溯

## 动态规划

定义dp矩阵和边界条件

python定义二维矩阵

dp = [[i for i in range(len_1)] for j in range(len_2)]

## 双指针

快慢指针

两头指针

在处理数组和链表相关问题时，双指针技巧是经常用到的，双指针技巧主要分为两类：**左右指针**和**快慢指针**

如果是提到有序数组 就可以想到双指针 因为双指针遍历比直接循环的时间复杂度小很多

```python
# 基本句式
while(left < right):
  # 终止条件
  # eg:
  if nums[left] + nums[right] == target:
     return 
  # 或者 如果是接雨水的话 就是left == right 就算return了  所以 while里面是left<=right
  if xxx:
    left += 1
  else:
    right -= 1
    
```

接雨水

几个数之和 

移除数组(不增加额外空间)

下一个排列  其实排列类型的有点类似于回溯

[
\46. 全排列](https://leetcode.cn/problems/permutations/description/)[47. 全排列 II](https://leetcode.cn/problems/permutations-ii/description/)[60. 排列序列](https://leetcode.cn/problems/permutation-sequence/description/)