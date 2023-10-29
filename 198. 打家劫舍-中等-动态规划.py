'''
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。



示例 1：

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2：

输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

思路：
1。 状态  定义dp[i]为当前满足条件的最大值(算上当前值nums[i])
2. 转移方程 dp[i] 为 历史所有dp中的最大值+当前值 与 当前dp的比较中的最大值
（其实这里也可以理解算法2的方式了，dp表示到当前index的最大值，因为要么书值都是大于0 所以要么包含隔壁 要么包含自己）
3。 边界条件 因为不能连续 所以1 2算是边界值，如果数组长度小于2 二者之间智能选一个
    所以后面的计算从index=2开始
'''

from typing import List
# 我的解法 使用了双层for循环 更慢一点
class Solution:
    def rob(self, nums: List[int]) -> int:
        for i in range(2, len(nums)):
            temp_num = nums[i]
            for j in range(i - 1):  # i-2+1
                nums[i] = max(nums[i], nums[j] + temp_num)
        nums.sort()  # 找到所有dp中的最大值

        return nums[-1]
# 之前的解法
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0] * N
        dp[0] = nums[0]
        if N>=2:
            dp[1] = max(nums[0],nums[1])
        for k in range(2, N):
            dp[k] = max(dp[k-1], nums[k] + dp[k-2])
        return dp[N-1]


