from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array = {}
        
        # Example: nums = [2,2,11,7,15], target = 9 
        for n in range(len(nums)): #range(5) -> 0,1,2,3,4
            difference = target - nums[n]
            
            if difference in array:
                return [array[difference], n]  # stored index first, current index second
            array[nums[n]] = n

nums = [2, 2, 11,7, 15]
target = 9
result = Solution().twoSum(nums, target)
print(result)
