# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order_list = []

# Launch the store and present a greeting to the customer
print("\nWelcome to the variety food truck.\n")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("\nType menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"\nWhat {menu_category_name} item would you like to order?\n")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
                    
            # 2. Ask customer to input menu item number
            menu_item_selection = input('\nEnter a menu item to purchase: ')

            # 3. Check if the customer typed a number
            if menu_item_selection.isnumeric():

                # Convert the menu selection to an integer
                menu_item_selection_int = int(menu_item_selection)
                
                # 4. Check if the menu selection is in the menu items
                if menu_item_selection_int in menu_items:
            
                    # Store the item name as a variable
                    valid_menu_item_selection = menu_items[menu_item_selection_int]

                    # Ask the customer for the quantity of the menu item
                    menu_item_selection_quantity = input('\nEnter a quantity to purchase: ')

                    # Check if the quantity is a number, default to 1 if not
                    if menu_item_selection_quantity.isnumeric():
                    
                        # Convert the quantity to an integer
                        menu_item_selection_quantity =int(menu_item_selection_quantity)
               
                    else:
                        # Convert the default quantity to an integer
                        menu_item_selection_quantity = 1

                    # Add the item name, price, and quantity to the order list
                    order_list.append({
                        "Item name": valid_menu_item_selection["Item name"],
                        "Price": valid_menu_item_selection["Price"],
                        "Quantity": menu_item_selection_quantity
                        })

                else:
                    # Tell the customer that their input isn't valid
                    menu_item_selection = input('Enter a valid menu item to purchase: ')
            
            else:
                # Tell the customer they didn't select a menu option
                menu_item_selection = input('Enter a valid menu item to purchase: ')

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")
        
    # Ask the customer if they would like to order anything else
    keep_ordering = str.upper('')
    
    # while false loop with check for non-standard input
    while (keep_ordering not in ('Y', 'N')):
        keep_ordering = str.upper(input('\nWould you like to keep ordering? (Y)es or (N)o '))
        
    # 5. Check the customer's input
    # Keep ordering
    match keep_ordering:
        case 'Y':
            print('\nAwesome! Let\'s order more! \n')
            
    # Stop ordering
        case 'N':
        # Since the customer decided to stop ordering, thank them for
        # their order
            print('\nYou made great choices! Thank you for your order! \n')
            
            # Exit the keep ordering question loop
            break
            
# Complete the order
place_order = False

# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print("Item name                 | Price  | Quantity")
#print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
#for key, value in order_list():
# Define and set total cost to zero
total_cost = 0
item_name_length_list = []
max_length = 26
min_length = 9

for item in order_list:

    # 7. Store the dictionary items as variables
    item_name = item["Item name"]
    price = item["Price"]
    quantity = item["Quantity"]

    # 8. Calculate the number of spaces for formatted printing
    item_name_length_list.append(len(item_name))
    item_name_length = len(item_name)
    break

# Find max and min lengths for item names
#print(order_list)
max_length = max(item_name_length_list)
min_length = len("Item Name")
print(max_length)
print(min_length)

# 9. Create space strings
# Conditional for variable header length
#if max_length > min_length:
if max_length > 9:
    print("Item Name" + " " * (item_name_length - min_length), "| Price  | Quantity")
    print("-" * (max_length+1) + "|--------|----------")
   
else:
    print("Item Name" + " " * (item_name_length - min_length), "| Price  | Quantity")
    print("-" * (min_length+1) + "|--------|----------")
    
# 10. Print the item name, price, and quantity
for item in order_list:
    print(f"{item['Item name']:<9} | ${item['Price']:<5.2f} | {item['Quantity']:<8}")
    
# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
total_cost = sum(item["Price"] * item["Quantity"] for item in order_list)
print(f"\nTotal Cost: ${total_cost:.2f}\n")
