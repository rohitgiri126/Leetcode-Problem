# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        carry = 0
        
        # Jab tak l1, l2 ya carry mein se kuch bhi bacha hai
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Total sum calculate karo
            total_sum = val1 + val2 + carry
            
            # Naya carry aur current digit nikalo
            carry = total_sum // 10
            digit = total_sum % 10
            
            # Nayi node create karke connect karo
            tail.next = ListNode(digit)
            tail = tail.next
            
            # Pointers ko aage badhao agar nodes bache hain
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next