def deleteDuplicates(self, head: ListNode) -> ListNode:
    if head is None:
        return head
    prev_val = head.val
    prev_node = head
    dummy = head
    head = head.next
    while head is not None:
        if head.val == prev_val:
            prev_node.next = head.next
        else:
            prev_node = prev_node.next
            prev_val = prev_node.val

        head = head.next

    return dummy