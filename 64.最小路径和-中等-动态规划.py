from typing import List
'''
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
示例 1：
输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
下面我的解法是新建了dp数组 但是也可直接在原来的数组上直接计算

解题思路：
1。 定义状态  定义当前点的最小路径和为状态
2。 转移方程 dp[i][j]= min(dp[i-1][j],dp[i][j-1])+grid[i][j]
3。 要注意边界条件 即 i = 0 或者j = 0 的情况 一般的方式是先将边界条件进行初始化
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
        dp[0][0] = grid[0][0]
        for i in range(1,len(grid)):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1,len(grid[0])):
            dp[0][j] = dp[0][j-1]+ grid[0][j]
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                dp[i][j]= min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[len(grid)-1][len(grid[0])-1]
if __name__ == '__main__':
    so = Solution()
    print(so.minPathSum([[1]]))