class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node simplifies edge cases (e.g., swapping head)
        dummy = ListNode(0, head)
        prev = dummy
        
        while prev.next and prev.next.next:
            # Nodes to be swapped
            first = prev.next
            second = prev.next.next
            
            # Swapping
            first.next = second.next
            second.next = first
            prev.next = second
            
            # Move prev pointer forward by 2 nodes
            prev = first
            
        return dummy.next