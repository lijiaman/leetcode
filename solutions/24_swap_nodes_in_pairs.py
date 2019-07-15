def swapPairs(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head or not head.next:
        return head
    prev_node = ListNode(0)
    prev_node.next = head
    second = head.next
    while head and head.next:
        next_node = head.next
        prev_node.next = next_node
        head.next = next_node.next
        next_node.next = head
        prev_node = head
        head = head.next

    return second