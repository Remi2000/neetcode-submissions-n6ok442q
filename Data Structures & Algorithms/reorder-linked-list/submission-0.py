# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # ======================
        # Step 1: 找中点
        # ======================
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        # ======================
        # Step 2: 反转后半段
        # ======================
        prev = None
        cur = second

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # ======================
        # Step 3: 交错合并
        # ======================
        # prev 是反转后的后半段头
        second = prev
        first = head

        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2

        return
        



