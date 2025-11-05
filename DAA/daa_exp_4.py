def knapsack_01(values, weight, capacity):
    n=len(values)

    # create table for store maximum value for different subproblems
    # dp table dimensions: (n+1) x (capacity+1)
    dp = [[0 for _ in range(capacity+1)] for _ in range(n+1)]

    # build table dp[][] in bottom up manner
    for i in range(1, n+1):
        for w in range(0, capacity+1):
            if weight[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weight[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    # back track to find items selected
    selected_item = []
    i, w = n, capacity
    while i > 0 and w > 0:
        # if the value comes from including the item, it will be different from value without it
        if dp[i][w] != dp[i-1][w]:
            selected_item.append(i-1)
            w -= weight[i-1]
        i -= 1

    selected_item.reverse()

    return dp[n][capacity], selected_item

#example
if __name__=="__main__":
    values =[60,100,120]
    weight =[10,20,30]
    max_capacity = 50

    max_value, selected_items = knapsack_01(values,weight,max_capacity)

    print("Selected item : ")
    for item in selected_items:
        print(f"item withweight {weight[item]} & value {values[item]}")

    print(f"Maximum value achievable : {max_value}")