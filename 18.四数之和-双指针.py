from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        rs_list = []
        if len(nums) < 4:
            return []
        for i  in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left = j+1
                right = len(nums) - 1
                while(left < right):
                    temp = nums[i] + nums[j] + nums[left] + nums[right]
                    if temp == target:
                        rs_list.append([nums[i],nums[j],nums[left],nums[right]])
                        left += 1
                        # right -= 1
                        # 第三个数据去重
                        while(left < right and nums[left] == nums[left-1]):
                            left+=1
                        # while(left < right and nums[right] == nums[right+1]):
                        #     right -= 1
                    elif temp < target:
                        left += 1
                    else:
                        right-=1
        return rs_list
if __name__ == '__main__':
    so = Solution()
    print(so.fourSum([1,0,-1,0,-2,2],0))