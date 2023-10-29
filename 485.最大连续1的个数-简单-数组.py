from typing import List
'''
给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。

 

示例 1：

输入：nums = [1,1,0,1,1,1]
输出：3
解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
示例 2:

输入：nums = [1,0,1,1,0,1]
输出：2
 

提示：

1 <= nums.length <= 105
nums[i] 不是 0 就是 1.
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        max_len = 0
        temp_len = 0
        for indexi,i in enumerate(nums):
            if i==1:
                temp_len += 1
            if i == 0:
                temp_len = 0
            max_len = max(max_len,temp_len)
        return max_len


if __name__ == '__main__':
    so = Solution()
    print(so.findMaxConsecutiveOnes([1,1,0,1,1,1]))