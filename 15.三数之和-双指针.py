from typing import List

'''
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请

你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

 

示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
示例 2：

输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
示例 3：

输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。
 

提示：

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''
'''
双指针解法 时间复杂度更低
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 先排序
        # 重复的可以 但是下标必须不同 双层遍历  然后判断剩下那个在不在数组中  如果在 就保存
        # 使用了3个for循环 超时了
        nums.sort()
        length = len(nums)
        rs_list = []
        if length < 3 or (nums[0] + nums[1]) > 0:
            return rs_list
        for indexi in range(0,length-2):
            # 相当于剪枝 不要也可以
            # if nums[indexi] > 0:
            #     break
            if indexi > 0 and nums[indexi-1] == nums[indexi]:
                continue
            target = -nums[indexi]
            left = indexi+1
            right = length -1
            while(left < right):
                # 相当于剪枝 不要也可以
                # if nums[left] > 0:
                #     break
                if nums[left] + nums[right] == target:
                    rs_list.append([nums[indexi],nums[left],nums[right]])
                    left+=1
                    #right-=1
                    # 第2个数去重  这个不去也可以
                    while left < right and nums[left-1] == nums[left]:
                        left += 1
                    # while left < right and nums[right+1] == nums[right]:
                    #     right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1

        return rs_list

'''
下面一个是自己写的解法  但是其实从中也可以看出双指针的端yi，相当于后面两个循环采取了同向剪枝  
但是其实可以用双指针 从两头开始往中间 内部的时间复杂度为o(n)，总体的时间复杂度为o(n^2) + o(n*logn)后面为数组排序
整体还是o(n^2)的复杂度
'''

class Solution_origin:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 先排序
        # 重复的可以 但是下标必须不同 双层遍历  然后判断剩下那个在不在数组中  如果在 就保存
        # 使用了3个for循环 超时了
        nums.sort()
        length = len(nums)
        rs_list = []
        if length < 3 or (nums[0] + nums[1]) > 0:
            return rs_list
        for indexi,i in enumerate(nums[:length-2]):
            if i > 0:
                break
            for indexj in range(indexi+1,length-1):
                j = nums[indexj]
                if (i + j) > 0:
                    break
                for indexk in range(indexj+1,length):
                    k = nums[indexk]
                    if k > -(i+j):
                        break

                    if k == -(i+j)  and [i,j,k] not in rs_list:
                        # print(i,j,k)
                        rs_list.append([i,j,k])
                        break
        return rs_list
if __name__ == '__main__':
    so = Solution()
    print(so.threeSum([-1,0,1,2,-1,-4]))