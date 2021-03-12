"""
Given an array A consisting of N distinct integers and another array B
consisting of M integers, you need to find the min number of elements to be 
added in B so that A becomes a sub-sequence of B, we can add at any position
in array B.

Example:
A = [1,2,3,4,5]
B = [2,5,6,4,9,12]

"""

def subsequence(A, B):
    min_number = float("inf")
    n = len(A)
    m = len(B)
    table = [[0 for i in range(m+1)] for j in range(n+1)]    


    #least common subsequence
    for i in range(1, n+1):
        for j in range(1, m+1):
            if A[i-1] == B[j-1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
	    
    #subtract n by lcs, return this 
    min_number = n - table[-1][-1]

    return min_number

print(subsequence([1,2,3,4,5], [2,5,6,4,9,12]))


