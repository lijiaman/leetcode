"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""

# 0. My original ugly solution
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

# 1. Updated version with dictionary
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        data_dict = {}
        p = head
        while p:
            data_dict[p] = Node(p.val, None, None)
            p = p.next

        p = head
        while p:
            if p.next:
                data_dict[p].next = data_dict[p.next]
            if p.random:
                data_dict[p].random = data_dict[p.random]
            p = p.next

        return data_dict[head]

# 2. Not using dictionary
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        p = head
        while p:
            node = Node(p.val, None, None)
            node.next = p.next
            p.next = node
            p = p.next.next

        p = head
        while p:
            node = p.next
            if p.random:
                node.random = p.random.next
            p = p.next.next

        p = head
        start = head.next
        while p and p.next:
            node = p.next
            p.next = p.next.next
            if p.next:
                node.next = p.next.next
            p = p.next

        return start
