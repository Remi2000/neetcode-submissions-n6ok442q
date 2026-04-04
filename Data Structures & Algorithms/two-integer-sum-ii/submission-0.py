class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            t = numbers[left] + numbers[right]
            if t == target:
                break
            elif t < target:
                left += 1
            elif t > target:
                right -= 1
        return [left + 1, right + 1]