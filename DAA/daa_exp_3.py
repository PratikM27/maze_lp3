class item:
    def __init__(self,weight,value):
        self.weight= weight
        self.value = value

def  fractional_knapsack(items, capacity):
    # calculate ration value/weight for each item
    value_weight_ratio = [(item.value / item.weight, item) for item in items]

    # sort in descending order
    value_weight_ratio.sort(reverse=True)

    total_value = 0
    knapsack = []

    for ratio, item in value_weight_ratio:
        if capacity == 0 :
            break

        weight = min(item.weight,capacity)
        total_value += weight * ratio
        capacity -= weight

        knapsack.append((item, weight))
    return total_value, knapsack

#Example

if __name__=="__main__":
    items = [item(10,60),item(20,100),item(30,120)]
    max_capacity = 50

    max_value, selected_value = fractional_knapsack(items,max_capacity)

    print("\nSelected items : ")
    for item, weight in selected_value:
        print(f"item with weight {item.weight} & value {item.value} Fraction take : {weight/item.weight}")
        print("Maximum value achievable :", max_value)



# ✔️ Time Complexity: O(n log n) (because of sorting)
# ✔️ Space Complexity: O(n)
# A knapsack (bag) that can hold a certain maximum weight (capacity).

# A set of items, each having:

# a weight

# a value (profit)