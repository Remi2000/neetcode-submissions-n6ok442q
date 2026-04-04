class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        pairs = list(count.items())

        pairs.sort(key = lambda p: (p[1], p[0]), reverse = True)

        return [num for num, count in pairs[:k]]