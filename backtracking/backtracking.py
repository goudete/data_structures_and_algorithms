"""
Generate all possibilites

Steps:
1. Generate decision tree as you go
2. Traverse in a DFS fashion
3. Prune unnecessary branches accordingly
4. Store results

Complexities:
Horribly innefficient (you are generating all possibilites)

Analysis:
- To generate all subsets: O(2^n)
- To generate all permutations: O(n!)
- Anything else: O(branching_factor^depth)
"""


#Generate all subsets of an array
def subsets(nums):
    res = []
    partial_sol = []

    def backtrack(index):
        #base case (subset is smaller than nums => use index)
        if index == len(nums):
            res.append(partial_sol[:])

        #general case
        else:
            partial_sol.append(nums[index])
            backtrack(index+1)
            partial_sol.pop()
            backtrack(index+1)

    backtrack(0)
    return res


#Generate all permutations of an array
def permutations(nums):
    res = []
    partial_sol = []

    def backtrack():
        #base case
        if len(partial_sol) == len(nums):
            res.append(partial_sol[:])

        #general case
        else:
            for num in nums:
                if num not in partial_sol:
                    partial_sol.append(num)
                    backtrack()
                    partial_sol.pop()
    backtrack()
    return res

# print(permutations([1,2,3]))
# print(subsets([1,2,3]))
