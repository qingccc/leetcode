'''
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。



示例 1：



输入：[1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
示例 2：

输入：height = [1,1]
输出：1


提示：

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
'''
'''
思路：可以储存的最大的水 取决于长和高(高取决于左右两侧短的这条线) 假设已经有了一个面积  那么对于2个柱子内部的(相当于长变短了) 
除非内部的柱子更高才有可能拥有更大的面积
对于2条柱子 短的向内移动 可能获得最大面积的可能性更大 对于高的 就先固定 直到2个柱子都走向中间
'''
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0
        while l <= r:
            max_area = max(max_area,(r-l) * min(height[l],height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area
if __name__ == '__main__':
    so = Solution()
    test = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(so.maxArea(test))
