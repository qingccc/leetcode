from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        right = 0
        tmp_sum = 0
        # min_len = 100001
        min_len = len(nums)+1
        if sum(nums) < target:
            return 0

        while left <= right and right < len(nums):
            if tmp_sum + nums[right] < target:
                tmp_sum += nums[right]
                right += 1
            else:
                tmp_sum += nums[right]
                while left <= right and tmp_sum >= target:
                    min_len = min(min_len, right - left + 1)
                    tmp_sum -= nums[left]
                    left += 1
                right += 1
        while left < right and tmp_sum >= target:
            min_len = min(min_len, right - left)
            tmp_sum -= nums[left]
            left += 1

        return min_len
# 用for循环更简单
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        win_sum = 0
        min_len = 100001
        if target > sum(nums):
            return 0
        for r,num in enumerate(nums):
            win_sum +=num
            while win_sum >= target:
                min_len = min(min_len,r-left+1)
                win_sum -= nums[left]
                left+=1
        return min_len

