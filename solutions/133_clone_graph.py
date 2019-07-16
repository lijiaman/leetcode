"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""

# 1. BFS---Queue
import collections
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        copy_node = Node(node.val, [])
        data_dict = {node: copy_node}
        queue = collections.deque([node])
        while queue:
            curr_node = queue.popleft()
            neighs = curr_node.neighbors
            for n in neighs:
                if n not in data_dict:
                    data_dict[n] = Node(n.val, [])
                    data_dict[curr_node].neighbors.append(data_dict[n])
                    queue.append(n)
                else:
                    data_dict[curr_node].neighbors.append(data_dict[n])

        return copy_node

# 2. DFS Iteratively---Stack
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        data_dict = {}
        copy_node = Node(node.val, [])
        stack = [node]
        data_dict[node] = copy_node
        while stack:
            curr = stack.pop()
            for n in curr.neighbors:
                if n not in data_dict:
                    data_dict[n] = Node(n.val, [])
                    stack.append(n)
                    data_dict[curr].neighbors.append(data_dict[n])
                else:
                    data_dict[curr].neighbors.append(data_dict[n])
        return copy_node
