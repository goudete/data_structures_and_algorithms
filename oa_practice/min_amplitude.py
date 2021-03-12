"""
Given an Array A, find the minimum amplitude you can get after changing up
to 3 elements. Amplitude is the range of the array (basically difference
between largest and smallest element).

Example 1:
Input: [-1, 3, -1, 8, 5, 4]
Output: 2
Explanation: we can change -1, -1, 8 to 3, 4 or 5

[-1,-1,3,4,5,8]
  ^  ^ ^

[-1,-1,3,4,5,8]
  ^  ^       ^

[-1,-1,3,4,5,8]
  ^        ^ ^

[-1,-1,3,4,5,8]
         ^ ^ ^

Example 2:
Input: [10, 10, 3, 4, 10]
Output: 0
Explanation: change 3 and 4 to 10

[3,4,10,10,10]

"""

# O(nlogn)
def min_amplitude(A):
    if len(A) <= 3:
        return 0

    min_amp = float("inf")

    # O(nlogn)
    A.sort()

    # two pointer approach?
    i, j = 3, len(A)-1

    # O(n)
    while i >= 0:
        min_amp = min(abs(A[i]-A[j]), min_amp)
        i -= 1
        j -= 1

    return min_amp

# print(min_amplitude([-1, 3, -1, 8, 5, 4]))
print(min_amplitude([10, 10, 3, 4, 10]))
