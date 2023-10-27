""" You are the manager of a supermarket. 
You have a list of  items together with their prices that consumers bought on a particular day. 
Your task is to print each item_name and net_price in order of its first occurrence.

item_name = Name of the item. 
net_price = Quantity of the item sold multiplied by the price of each item.

Input Format:
The first line contains the number of items, N. 
The next N lines contains the item's name and price, separated by a space.

Constraints:
0 < N <= 100

Output Format:
Print the item_name and net_price in order of its first occurrence.

Sample Input:
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

Sample Output:
BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20 """

from collections import OrderedDict

# Read the number of items from the user
n = int(input())

# Create an ordered dictionary to store items and their total prices in the order of insertion
items = OrderedDict()

# Iterate through the input and calculate net prices for each item
for _ in range(n):
    input_line = input().split()
    # Extract item name (which can contain multiple words) and price from the input
    item_name = ' '.join(input_line[:-1])
    price = int(input_line[-1])
    # If the item is already in the ordered dictionary, update its price
    if item_name in items:
        items[item_name] += price
    # If the item is encountered for the first time, add it to the ordered dictionary
    else:
        items[item_name] = price

# Print item names and net prices in the order of their first occurrence
for item_name, net_price in items.items():
    print(item_name, net_price)