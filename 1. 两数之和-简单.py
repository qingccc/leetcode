from typing import List
'''
https://leetcode.cn/problems/two-sum/description/ 
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。
1. 仔细看题，题目说数组中同一个元素在答案中不能重复出现，但是可以出现两个元素的值得相同。
思路：
1. 先找到第一个  然后在剩下的里面找另外一个
* 第一个的判断 是如果在nums中存在  并且 target-num 的下标 应该是在后面的里面会出现  
2. 在剩下的里面找到第二个，如果找到就return 否则return空

'''

# 方案1  暴力解法
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first = 0
        for index, i in enumerate(nums):
            # 并且不是这个index
            if (target - i) in nums and (target - i) in nums[index + 1:]:
                first = index
                break
        second = 0
        for index, i in enumerate(nums[first + 1:]):
            if i == target - nums[first]:
                second = index + first + 1
                return [first, second]
        return []
# 方案2 使用dict,hash映射
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_dict = {}
        for index, i in enumerate(nums):
            map_dict[i] = index # 如果重复 就是返回最新的
        for index, i in enumerate(nums):
            if (target - i) in map_dict and map_dict[i]!=index:
                return [index,map_dict[i]]
        return []
if __name__ == '__main__':
    so = Solution()
    print(so.twoSum([3,3,3],6))