# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ptr = head
        visited = []
        while ptr:
            if ptr in visited:
                return True
            visited.append(ptr)
            ptr = ptr.next
        return False