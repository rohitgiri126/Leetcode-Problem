class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next  # 1. Save next node
            curr.next = prev       # 2. Reverse current node's pointer
            prev = curr            # 3. Move prev forward
            curr = next_node       # 4. Move curr forward
            
        return prev  # New head of the reversed list