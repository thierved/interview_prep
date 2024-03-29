"""
   ==================  Day 1: Linked List ================
        Problem: Middle of the linked list.

"""

def middle_node(head, node_list):
    slow = head
    fast = head
    while (fast and fast.next):
        slow = node_list.next
        fast = node_list.next.next
    return slow

