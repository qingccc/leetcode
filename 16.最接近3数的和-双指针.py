'''
给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。

返回这三个数的和。

假定每组输入只存在恰好一个解。



示例 1：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
示例 2：

输入：nums = [0,0,0], target = 1
输出：0

'''

from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 思路：先排序 固定第一个数 剩下2个使用双指针
        nums.sort()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            rs_sum = nums[0] + nums[1] + nums[2]  # 用来保存结果
            while (left < right):
                temp = (nums[i] + nums[left] + nums[right])
                if target == temp:
                    return target
                if abs(target - temp) < abs(target - rs_sum):
                    rs_sum = target
                # 用来找到目标值,并实现遍历数组的目的
                if temp < target:
                    left += 1
                else:
                    right -= 1
        return rs_sum
