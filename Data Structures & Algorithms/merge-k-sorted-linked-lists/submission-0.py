# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 时间	O(N log k)	N = 所有节点总数，每个节点 push/pop 一次，堆大小 k → 每次 O(log k)
        # 空间	O(k)	堆最多同时存 k 个节点
        heap = []
        
        # 把每个链表的头节点放进堆
        for i, node in enumerate(lists):
            if node:
                # (值, 链表编号, 节点) — 编号用来防止值相同时比较节点报错
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode()
        curr = dummy

        while heap:
            # 弹出最小的节点
            val, i, node = heapq.heappop(heap)
            
            # 接到结果链表上
            curr.next = node
            curr = curr.next

            # 如果这个节点还有 next，放进堆里
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next