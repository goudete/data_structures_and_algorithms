
"""
Binary Search
Great for searching in a sorted array

Complexity:
Time: O(logn)
Space: O(1)

     l           r
[0,1,2,3,4,5,6,7,8]
"""


def binary_search(nums, target):
    l, r = 0, len(nums)-1

    while l+1 < r:
        mid = (l+r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid
        else:
            l = mid

    if l == target: return l
    if r == target: return r
    return -1

print(binary_search([1,4,16,34,40,55,67,79,90], 55))
