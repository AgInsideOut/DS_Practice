""" One common use for dicts is as a small database within our program. We set up the dict at the top of the program, 
and then reference it throughout the program.
For example, you might set up a dict of months, with the month names as keys and numbers as values. Or perhaps you’ll 
have a dict of users, with user IDs as the keys and email addresses as the values.

In this exercise, I want you to create a new constant dict, called MENU, representing the possible items you can order 
at a restaurant. The keys will be strings, and the values will be prices (i.e., integers). You should then write a 
function, restaurant, that asks the user to enter an order:
If the user enters the name of a dish on the menu, the program prints the price and the running total. It then asks 
the user again for their order.
If the user enters the name of a dish not on the menu, the program scolds the user (mildly). It then asks the user 
again for their order.
If the user enters an empty string, the program stops prompting and prints the total amount.
For example, a session with the user might look like this:

Order: sandwich
sandwich costs 10, total is 10
Order: tea
tea costs 7, total is 17
Order: elephant
Sorry, we are fresh out of elephant today.
Order: 
Your total is 17

Note that you can always check to see if a key is in a dict with the in operator. That returns True or False. """

# Create a constant dictionary representing the restaurant menu
MENU = {
    "sandwich": 10,
    "tea": 7,
    "salad": 8,
    "pizza": 12,
    "burger": 9,
    "soup": 6,
    "pasta": 11,
    "smoothie": 5,
    "cake": 6,
    "ice cream": 4,
    "coffee": 3,
    "fruit salad": 7,
    "sushi": 14,
    "burrito": 10,
    "pancake": 5
}

# Create a function restaurant
def restaurant():
    total = 0  # Initialize the total variable to keep track of the running total

    print("Hello, welcome to VeggieHoot restaurant!")
    print("Menu: ", list(MENU.keys()))  # Print the available menu items

    while True:
        item = input("Please enter the item you want to order (or press Enter to finish): ").lower()

        # Check if the user wants to finish the order
        if item == "":
            print(f"Your total is ${total}")
            break

        # Check if the item is in the menu
        elif item in MENU:
            price = MENU[item]
            total += price
            print(f"{item} costs ${price}, total is ${total}")

        # Handle case where the item is not in the menu
        else:
            print(f"Sorry, '{item}' is not available on the menu. Please choose something else.")

# Call the restaurant function to start taking orders
restaurant()
