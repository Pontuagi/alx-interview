#!/usr/bin/python3

'''
This Module contains one function.
The function determines if n number of Locked boxes can be opened
'''
from collections import deque


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened by traversing through the
    keys available in the boxes.

    Args:
    - boxes: A list of lists where each index represents a box and
    its content are the keys to other boxes.

    Returns:
    - True if all boxes can be opened, else False.
    """
    if not boxes or len(boxes) == 1:
        return True

    visited = set()
    queue = deque([0])

    # Perform Breadth-First-Search traversal through the boxes.
    while queue:
        current_box = queue.popleft()
        visited.add(current_box)

        # Check keys in the current box and add unvisited boxes to the queue.
        keys = boxes[current_box]
        for key in keys:
            if key not in visited and key < len(boxes):
                queue.append(key)

    return len(visited) == len(boxes)
