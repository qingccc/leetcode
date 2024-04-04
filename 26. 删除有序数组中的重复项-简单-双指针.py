'''
给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。

考虑 nums 的唯一元素的数量为 k ，你需要做以下事情确保你的题解可以被通过：

更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，并按照它们最初在 nums 中出现的顺序排列。nums 的其余元素与 nums 的大小不重要。
返回 k 。
判题标准:

系统会用下面的代码来测试你的题解:

int[] nums = [...]; // 输入数组
int[] expectedNums = [...]; // 长度正确的期望答案

int k = removeDuplicates(nums); // 调用

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
如果所有断言都通过，那么您的题解将被 通过。

示例 1：

输入：nums = [1,1,2]
输出：2, nums = [1,2,_]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。
示例 2：

输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。
'''

'''
根据题解 返回的是一个数组 数组后面的长度不考虑 只截取前k进行assert比较 
思路： 移动数组类型 主要方法是将要移除的数据和后面的进行交换；
该题数组本来就是一个递增的数组 因此只要保证把每次数值不同的数据放到最前面k个就行  主要是通过nums[i]！=nums[i-1]判断
找到了之后直接移动过去就行 也不用担心会把其他数据覆盖 因此要覆盖的必定是小于该数并且重复的数据，主要记录对应的index就行
'''
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0

        for i in nums[1:]:
            # print(i)
            if i != nums[index]:
                index += 1
                nums[index] = i
                # print("111",nums[index])
        return index + 1