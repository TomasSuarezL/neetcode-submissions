# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        node = head
        aux = []
        while node is not None:
            aux.append(node.val)
            node = node.next

        new_head = ListNode(aux[-1])
        cur = new_head
        for item in aux[:-1][::-1]:
            new_node = ListNode(item)
            cur.next = new_node
            cur = new_node

        return new_head
