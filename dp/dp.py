
class DP:
    """
    Knapsack Problem
    You are a bank robber and are currently inside of a vault.
    The vault has n objects with weight w and value v.

    Your knapsack can only hold weight W. What is the
    maximum value you can carry?

    objects = [(v1, w1), (v2, w2), (vn, wn)]
    """

    def __init__(self, objects, W):
        self.objects = objects
        self.max_weight = W

    def fill_knapsack(self):
        """
        1. Create dp table
        2. Base cases?
        3. Fill iteratively
        """
        m, n = len(self.objects), self.max_weight

        table = [[0 for i in range(n+1)] for j in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                value, weight = self.objects[i-1]
                if weight <= j:
                    table[i][j] = max(value + table[i-1][j-weight], table[i-1][j])
                else:
                    table[i][j] = table[i-1][j]
        print(table[-1][-1])

#Knapsack
knapsack = DP([(60, 5), (50, 3), (70, 4), (30, 2)], 5)
knapsack.fill_knapsack()

def matrix_practice():

    m, n = 2, 3

    table = [[0 for i in range(n+1)] for j in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            table[i][j] = 1
    print(table)

# matrix_practice()
