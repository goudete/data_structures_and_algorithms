"""
-Problem Statement-
Select from arr1 but you can only select numbers from
left or right (select K times). Then, the first element
we select from arr1 is multiplied by the first number
in arr2. The 2n number we select from arr1 is multiplied
by the 2nd number in arr2. so on and so forth. The
multiplication results will be summed together. Return
the maximum final result possible.

Example:
arr1 =[1, 8, 7, 10], arr2 = [3, 11, 5], K = 3

max sum is 153
explain: maximum_sum = 3*1+11*10+5*8 = 153


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


High level:
    - Optimizing for max sum
    - Optimal substructure: each individual product => DP
    - Overlapping subproblems(?)

    At each step, we can pick from left or right (from arr1)

    Essentially, this can be represented by a 3d dp table

    m => pick left
    n => pick right
    k => arr2 value

    General case:
    # at each step, we can pick left or right
    # we aggregate by looking at previous left and right and calculating current left and right

    dp[curr_pick_left][curr_pick_right][curr_k] =
            #looks left
        max(dp[curr_pick_left-1][curr_pick_right][curr_k-1]+arr1[curr_pick_left]*arr2[curr_k],
            #looks right
            dp[curr_pick_left][curr_pick_right-1][curr_k-1]+arr1[-curr_pick_right]*arr2[curr_k])

    Base case:
    - dp[0][0][0] = 0

"""

def max_sum(arr1, arr2, k):
    max_sum = 0
    m = n = len(arr1)

    dp_table = [[[0 for i in range(k)] for j in range(n)] for z in range(m)]
    print(dp_table)

    #base case
    dp_table[0][0][0] = 0

    #general case
    for curr_pick_left in range(m):
        for curr_pick_right in range(n):
            for curr_k in range(k):

                dp_table[curr_pick_left][curr_pick_right][curr_k] = max(dp_table[curr_pick_left-1][curr_pick_right][curr_k-1]+arr1[curr_pick_left]*arr2[curr_k],
                    dp_table[curr_pick_left][curr_pick_right-1][curr_k-1]+arr1[-curr_pick_right]*arr2[curr_k])


    print(dp_table)

max_sum([1, 8, 7, 10], [3, 11, 5], 3)
