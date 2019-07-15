"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        data_dict = {}
        data_dict[head] = Node(head.val, None, None)
        prev = head
        p = head.next
        while p:
            data_dict[p] = Node(p.val, None, None)
            data_dict[prev].next = data_dict[p]
            prev = p
            p = p.next

        p_r = head
        while p_r:
            r_node = p_r.random
            if r_node:
                if r_node not in data_dict:
                    data_dict[r_node] = Node(r_node.val, None, None, None)
                    data_dict[p_r].random = data_dict[r_node]
                else:
                    data_dict[p_r].random = data_dict[r_node]
            p_r = p_r.next

        return data_dict[head]