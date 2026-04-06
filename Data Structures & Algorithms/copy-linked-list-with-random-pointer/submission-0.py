"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 时间    O(n)    两次遍历链表
        # 空间    O(n)    哈希表存 n 个节点映射
        if not head:
            return None

        mapping = {}

        # 第一次遍历：创建所有新节点
        cur = head
        while cur:
            mapping[cur] = Node(cur.val)
            cur = cur.next

        # 第二次遍历：连接 next 和 random
        cur = head
        while cur:
            mapping[cur].next = mapping.get(cur.next)      # cur.next 可能是 None
            mapping[cur].random = mapping.get(cur.random)   # cur.random 可能是 None
            cur = cur.next

        return mapping[head]