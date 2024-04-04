from typing import List
'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

示例 1：
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
示例 2：

输入：height = [4,2,0,3,2,5]
输出：9
 

提示：

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        # 每个方块自己的顶部的水  加起来就是最后能接多少的雨水
        # 每个方块找到左边的最高  和 右边的最高 用dp表示  dp[i] = max(dp[i-1],h[i-1])
        dp_l = [0] * len(height)
        dp_r = [0] * len(height)
        dp_l[0] = 0
        dp_r[len(height)-1] = 0
        length = len(height)
        rs_sum = 0
        for index in range(1,length):
             dp_l[index] = max(dp_l[index-1],height[index-1])
        # print(dp_l)
        for index in range(length-2,-1,-1):
            dp_r[index] = max(dp_r[index+1],height[index+1])
        # print(dp_r)

        for index, i in enumerate(height):
            # print(dp_l[index],dp_r[index],i)
            temp = min(dp_l[index],dp_r[index]) - i if min(dp_l[index],dp_r[index]) > i else 0
            rs_sum += temp
        return rs_sum
if __name__ == '__main__':
    so = Solution()
    print(so.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(so.trap([4,2,0,3,2,5]))