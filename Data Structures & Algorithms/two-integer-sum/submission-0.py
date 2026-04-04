class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i, n in enumerate(nums):
            need = target - nums[i]
            if need in cache:
                return [cache[need], i]
            
            cache[n] = i
        