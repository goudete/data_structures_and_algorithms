

"""
Implementing min/max heap (Also called Priority Queue)

A heap is essentially a Binary Tree
with the following properties:

For Max Heap:
- root of each subtree >= its children
- balanced

For Min Heap:
- root of each subtree <= its children
- balanced

Complexities:
- Max/Min look up => O(1)
- Pop root => heapify?
- Insert => O(logn) (to find place) + heapify?

Implementation:
Heaps are implemented using an array, where:
heap[k] <= heap[2*k+1] (left child)
heap[k] <= heap[2*k+2] (right child)

In python, use heapq module

Basic operations:
"""
import heapq

li = [5,6,4,3,7,8,9]

#creating heap
heapq.heapify(li)

#push elements into heap
heapq.heappush(li, 4)

#pop smallest element (root)
heapq.heappop(li)

#peak root
li[0]
