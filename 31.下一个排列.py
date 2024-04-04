from typing import List
'''
思路： 1. 先在纸上根据用例列一列 2. 尽量考虑到所有特殊情况
本题的思路是  从右边遍历数组，先从最右边找到第一个小于该数的值，如果找到就break 否则继续循环
  然后进行交换  再把交换完后的index 后的数组按照正序排列(这样可以保证交换完后后面的顺序是最小序，应该使用到排序的方法)；
  注意到 index 后面的数已经是从大到小排列了（非严格递减），我们其实只需要用双指针交换即可，而不需要真正地排序。

index后面的数一定是从大到小排好序了吗？当然，否则，我们找到第一个可以交换的回溯点就不是 index 了，和 index 是第一个可以交换的回溯点矛盾。因为第一个可以交换的回溯点其实就是从后往前第一个递减的值。
  特殊情况: 如果整个数组已经是最大序(整个都找不到比右侧数字小的数字)  那么就是返回整个数字的sort序列

参考下载下来的leetcode题库
写几个例子通常会帮助理解问题的规律
在有序数组中首尾指针不断交换位置即可实现 reverse 双指针
找到从右边起第一个大于nums[i]的，并将其和 nums[i]进行交换
'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # 找到第一个没有右边大的数i 那么肯定会交换
        # 找到最右边第一个大于i的数 保证交换后值最小
        # 后面的数据是属于降序的 所以把它变成正序 使用reverse 双指针快点
        i = len(nums)-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i-=1
        j = len(nums)-1
        if i >= 0:
            # 如果nums[j] 没有nums[i]大 就移动
            while j >= i and nums[i] >= nums[j]:
                j-=1
            # 交换
            nums[i], nums[j] = nums[j], nums[i]
        # 反转后面的数组
        left = i+1
        right = len(nums)-1
        while(left < right):
            nums[left],nums[right] = nums[right],nums[left]
            left += 1
            right -= 1
        return nums
class Solution_1:
    # 有问题 还没写好
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 从右侧找到第一个比他小的 交换
        for i in range(len(nums)-1,1,-1):

            index = i
            while(index > 0 and nums[index] <= nums[index-1]):
                index -= 1
            # print(index)
            # index = index -1
            if index >0 and nums[index] > nums[index-1]:
                index = index - 1
                # nums[index],nums[i] = nums[i],nums[index]
                # 剩下的往前移动  这个交换的数 肯定是在最后一个
                break
        print(i,index)
        if  index==i:
            return nums.sort()
        nums[index],nums[i] = nums[i],nums[index]
        print(nums[index],nums[i])
        test = nums[index+1:]
        test.sort()
        # index_te
        for k in range(index+1,len(nums)):
            nums[k] = test[k-index-1]
        return nums
if __name__ == '__main__':
    so = Solution()
    print(so.nextPermutation([4,4,1,3,4,2]))

    # so = Solution_1()
    # print(so.nextPermutation([4, 4, 1, 3, 4, 2]))