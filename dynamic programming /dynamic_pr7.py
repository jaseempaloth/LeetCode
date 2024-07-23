# delete and earn
from typing import List
from collections import Counter
class Solution:
    def deleteAndEarn(self, nums : list[int]) -> int:
        count = Counter(nums)
        nums = sorted(list(set(nums)))
        
        e1, e2 = 0, 0
        for i in range(len(nums)):
            cur_val = nums[i] * count[nums[i]]
            if i > 0 and nums[i] == nums[i - 1] + 1:
                temp = e2
                e2 = max(cur_val + e1, e2)
                e1 = temp
            else:
                temp = e2
                e2 = cur_val + e2
                e1 = temp
        return e2


