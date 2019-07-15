"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        copy_node = Node(node.val, [])
        data_dict = {node: copy_node}
        queue = [node]
        while len(queue) > 0:
            curr_node = queue.pop(0)
            neighs = curr_node.neighbors
            for n in neighs:
                if n not in data_dict:
                    data_dict[n] = Node(n.val, [])
                    data_dict[curr_node].neighbors.append(data_dict[n])
                    queue.append(n)
                else:
                    data_dict[curr_node].neighbors.append(data_dict[n])

        return copy_node