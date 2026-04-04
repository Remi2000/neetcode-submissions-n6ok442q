class TrieNode:
    def __init__(self):
        self.children = {}   # 字典：字符 -> 子节点
        self.is_end = False  # 标记这个节点是不是某个完整单词的结尾

class PrefixTree:
    # insert	O(m)	O(m)	m = word length, worst case create m new nodes
    # search	O(m)	O(1)	traverse m characters, no extra space
    # startsWith	O(m)	O(1)	same as search, skip is_end check
    def __init__(self):
        self.root = TrieNode()  # 根节点，不存任何字符

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:   # 这条路还不存在
                node.children[char] = TrieNode()  # 创建新节点
            node = node.children[char]  # 往下走一步
        node.is_end = True  # 整个单词走完了，标记终点

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:  # 路径断了，单词不存在
                return False
            node = node.children[char]
        return node.is_end  # 路径存在，但必须是完整单词才算找到

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:  # 路径断了，前缀不存在
                return False
            node = node.children[char]
        return True  # 路径存在就行，不管是不是完整单词

        
        