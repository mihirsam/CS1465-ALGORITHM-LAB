# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]

    # Build table K[][] in bottom up manner
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[n][W]

# Driver program to test above function
val = [5, 3, 4]
wt = [3, 2, 1]
W = 5
n = len(val)
print(knapSack(W, wt, val, n))

# This code is originally contributed by Bhavya Jain at: http://www.geeksforgeeks.org/dynamic-programming-set-10-0-1-knapsack-problem/

# adapted to solve the instance of 0-1 Knapsack problem descrived in this video: https://www.youtube.com/watch?v=EH6h7WA7sDw
