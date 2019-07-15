'''
Start from left-most and right-most edges to approach center. It can be regarded as a greedy algorithm.
The key is to realize if height[i] < height[j], the area of [i, j-k] must be smaller than [i, j], thus in this case,
we should move i right.
'''

def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    l_idx = 0
    r_idx = len(height) - 1
    max_area = 0
    while l_idx < r_idx:
        curr_area = min(height[l_idx], height[r_idx]) * (r_idx - l_idx)
        if curr_area > max_area:
            max_area = curr_area

        if height[l_idx] < height[r_idx]:
            l_idx += 1
        else:
            r_idx -= 1

    return max_area