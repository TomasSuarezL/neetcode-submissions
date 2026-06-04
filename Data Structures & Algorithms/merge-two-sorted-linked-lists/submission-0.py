# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr_1 = list1
        ptr_2 = list2
        new_list = None
        new_list_ptr = None
        while ptr_1 is not None or ptr_2 is not None:            
            if not ptr_2 or (ptr_1 and ptr_1.val <= ptr_2.val):
                new_node = ListNode(ptr_1.val)
                ptr_1 = ptr_1.next
            else:
                new_node = ListNode(ptr_2.val)
                ptr_2 = ptr_2.next
            
            if new_list:
                new_list_ptr.next = new_node
                new_list_ptr = new_node
            else:
                new_list = new_node
                new_list_ptr = new_node

        return new_list
