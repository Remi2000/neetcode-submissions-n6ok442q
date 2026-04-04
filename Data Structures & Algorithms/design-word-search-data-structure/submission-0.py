class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    # 操作	时间	空间	说明
    # addWord	O(m)	O(m)	same as 208 insert
    # search	O(26ⁿ)	O(m)	worst case all dots: each level branches 26 ways. n = number of dots. 
    # Space is recursion depth m

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # exactly the same as Trie insert
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            # 情况1: word 走完了，检查是不是完整单词
            if i == len(word):
                return node.is_end

            c = word[i]

            # 情况2: 普通字符，走固定的一条路
            if c != '.':
                if c not in node.children:
                    return False
                return dfs(node.children[c], i + 1)

            # 情况3: 通配符，尝试所有子节点
            else:
                for child in node.children.values():
                    if dfs(child, i + 1):  # 有一条走通就够了
                        return True
                return False  # 全部走不通
        return dfs(self.root, 0)