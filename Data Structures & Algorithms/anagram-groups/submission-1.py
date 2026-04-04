from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 时间复杂度 O(n * k log k); n是strs里面的总数, k是平均一个单词的长度
        # 空间复杂度 O(n * k);
        groups = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            groups[key].append(s)

        return list(groups.values())