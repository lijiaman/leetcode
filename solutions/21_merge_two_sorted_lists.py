'''
Iterative or Recursive solution.
'''


def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    dummy = ListNode(0)
    curr_node = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr_node.next = l1
            l1 = l1.next
        else:
            curr_node.next = l2
            l2 = l2.next
        curr_node = curr_node.next

    curr_node.next = l1 or l2

    return dummy.next