from typing import List
from collections import defaultdict
import random
class Solution:

    def __init__(self, nums: List[int]):
        # map 的每个值是一个list
        self.map = {}
        for index, num in enumerate(nums):
            if num in self.map:
                self.map[num].append(index)
            else:
                self.map[num] = [index]

    def pick(self, target: int) -> int:
        # 如果找不到 自己会返回null
        return random.choice(self.map[target])

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)