# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy 统一处理删除 head 的情况
        dummy = ListNode(0, head)
        fast = head
        slow = dummy

        # fast 先走 n 步，使得 fast 和 slow 之间相差 n 个节点
        for _ in range(n):
            fast = fast.next
        
        # fast 走到末尾时，slow 会停在待删除节点的前一个
        while fast:
            slow = slow.next
            fast = fast.next

        # 删除 slow.next（倒数第 n 个）
        slow.next = slow.next.next

        return dummy.next