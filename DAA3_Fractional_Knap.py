# Fractional Knapsack Problem (Greedy Approach)

class Item:
    """Stores weight, value, and value/weight ratio of each item"""

    def __init__(self, weight, value, index):
        self.weight = weight
        self.value = value
        self.index = index
        self.ratio = value / weight  # Calculate value per weight ratio


def fractional_knapsack(weights, values, capacity):
    """Function to find the maximum total value for the given capacity"""

    # Step 1: Create a list of item objects (weight, value, ratio)
    items = []
    for i in range(len(weights)):
        item = Item(weights[i], values[i], i)
        items.append(item)

    # Step 2: Sort items in descending order of ratio (value per weight)
    items.sort(reverse=True, key=lambda item: item.ratio)

    total_value = 0.0  # stores final maximum value

    # Step 3: Pick items greedily
    for item in items:
        if capacity >= item.weight:  # Take full item
            capacity -= item.weight
            total_value += item.value
        else:
            # Take fraction of item
            fraction = capacity / item.weight
            total_value += item.value * fraction
            capacity = 0
            break  # Knapsack is full

    return total_value


# Step 4: Input data
n = int(input("Enter number of items: "))
weights = []
values = []
for i in range(n):
    w = float(input(f"Enter weight of item {i+1}: "))
    v = float(input(f"Enter value of item {i+1}: "))
    weights.append(w)
    values.append(v)

capacity = float(input("Enter capacity of knapsack: "))

# Step 5: Function call
result = fractional_knapsack(weights, values, capacity)
print("Maximum value in Knapsack =", result)

"""
Sample Input:
Enter number of items: 4
Enter weight of item 1: 10
Enter value of item 1: 60
Enter weight of item 2: 40
Enter value of item 2: 40
Enter weight of item 3: 20
Enter value of item 3: 100
Enter weight of item 4: 30
Enter value of item 4: 120
Enter capacity of knapsack: 50

Sample Output:
Maximum value in Knapsack = 240.0
"""
