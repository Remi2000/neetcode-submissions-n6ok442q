# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Base case：0 或 1 个节点，不需要重排
        if not head or not head.next:
            return

        # ======================
        # Step 1: 找中点
        # ======================
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow 停在左中点
        # 第二段从 slow.next 开始
        second = slow.next
        slow.next = None    # 断开两段

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
            # 保存下一节点，防止断链
            tmp1 = first.next
            tmp2 = second.next

            # 交错连接
            first.next = second
            second.next = tmp1

            # 指针前进
            first = tmp1
            second = tmp2

        return
        



