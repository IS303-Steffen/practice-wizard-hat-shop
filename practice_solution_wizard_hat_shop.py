# Practice: Wizard Hat Shop – Order Queue
# Manage a queue of hat orders for a whimsical shop.

orders = []  # list of dicts: {"customer": str, "size": float, "enchantment": str}

def count_enchantment(orders_list, enchantment):
    """
    Return how many orders in orders_list have the given enchantment.
    Ignores capitalization and extra spaces in the enchantment argument.
    """
    target = enchantment.strip().lower() # make it work even if the captialization is different, or extra spaces included
    count = 0
    for order in orders_list:
        if order["enchantment"].strip().lower() == target:
            count += 1
    return count

def average_hat_size(orders_list):
    """
    Return the average hat size (float) across all pending orders.
    If there are no orders, return 0.0.
    """
    if len(orders_list) == 0: # return 0 first so we don't try to divide by 0 later on, which causes an error.
        return 0.0
    total = 0.0 # keep track of the total. Create the tracking variable outside of the loop
    for order in orders_list:
        total += order["size"]
    return total / len(orders_list)

print("Welcome to the Wizard Hat Shop - Order Queue!")

while True: # run forever until we choose the exit option.
    print("\nMenu:")
    print("1: Add an order")
    print("2: Fulfill next order")
    print("3: List all pending orders")
    print("4: Count orders by enchantment")
    print("5: Show average hat size")
    print("6: Exit")

    choice = input("Enter an option (1-6): ").strip()

    if choice == "1":
        customer = input("Customer name: ").strip()
        size = float(input("Hat size (e.g., 7.25): ").strip())
        enchantment = input("Enchantment (e.g., invisibility, luck, wisdom): ").strip().lower()

        order = {"customer": customer, "size": size, "enchantment": enchantment}
        orders.append(order)
        print(f"Added order for {customer}: size {size}, enchantment '{enchantment}'.")

    elif choice == "2":
        if len(orders) == 0:
            print("No pending orders to fulfill.")
        else:
            next_order = orders.pop(0)  # get rid of the first thing in the list
            print("Fulfilling order:")
            print(f"\tCustomer: {next_order['customer']}")
            print(f"\tSize: {next_order['size']}")
            print(f"\tEnchantment: {next_order['enchantment']}")

    elif choice == "3":
        if len(orders) == 0:
            print("No pending orders.")
        else:
            print("\nPending Orders:")
            for idx, order in enumerate(orders, start=1):
                print(f"{idx}. {order['customer']} | size {order['size']} | {order['enchantment']}")

    elif choice == "4":
        ench = input("Enter an enchantment to count: ")
        count = count_enchantment(orders, ench)
        print(f"There are {count} orders with enchantment '{ench.strip()}'.")
        
    elif choice == "5":
        avg = average_hat_size(orders)
        print(f"Average hat size across pending orders: {avg:.2f}")

    elif choice == "6":
        print("Closing the order book. May your hats fit and your charms never fizzle!")
        break

    else:
        print("Invalid choice, try again!")