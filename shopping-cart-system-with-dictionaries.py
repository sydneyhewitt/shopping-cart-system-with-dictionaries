# Import datetime to get the current date
from datetime import datetime

# Create a dictionary with five products and their prices
products = {
    "Chips": 2.00,
    "Soda": 2.50,
    "Candy": 1.50,
    "Cookies": 3.00,
    "Water": 1.00
}

# Create an empty shopping cart
shopping_cart = {}


# Function to display available products
def display_products(products):

    print("\n========== AVAILABLE PRODUCTS ==========")

    number = 1

    # Go through each product and display its price
    for product, price in products.items():

        print(str(number) + ". " + product + " - $" + str(price))

        number += 1


# Function to add a product to the shopping cart
def add_product(products, shopping_cart):

    # Display the available products
    display_products(products)

    product_names = []

    # Store product names in a list
    for product in products:
        product_names.append(product)

    # Ask the user to select a product
    num = int(input("\nEnter product number: "))

    # Check if the product number is valid
    while num < 1 or num > len(products):

        print("Invalid product!")

        num = int(input("Enter product number: "))

    # Get the selected product
    selected_product = product_names[num - 1]

    # Ask the user how many they want
    quantity = int(input("How many " + selected_product + " would you like to add? "))

    # Make sure the quantity is greater than zero
    while quantity <= 0:

        print("Quantity must be greater than 0!")

        quantity = int(input("How many " + selected_product + " would you like to add? "))

    # Add the quantity to the cart if the product already exists
    if selected_product in shopping_cart:

        shopping_cart[selected_product] += quantity

    # Otherwise, add the product to the cart
    else:

        shopping_cart[selected_product] = quantity

    # Display the updated cart quantity
    print("\nAdded " + str(quantity) + " " + selected_product + " to your cart!")

    print(selected_product + " quantity is now " + str(shopping_cart[selected_product]) + ".")


# Function to remove one product from the shopping cart
def remove_product(shopping_cart):

    # Check if the shopping cart is empty
    if len(shopping_cart) == 0:

        print("\nYour shopping cart is empty!")
        print("There is nothing to remove.")

        return

    else:

        print("\n========== YOUR SHOPPING CART ==========")

        cart_products = []

        # Store the cart product names in a list
        for product in shopping_cart:
            cart_products.append(product)

        number = 1

        # Display each product and its quantity
        for product, quantity in shopping_cart.items():

            print(str(number) + ". " + product + " - Quantity: " + str(quantity))

            number += 1

        # Ask the user which product to remove
        num = int(input("\nEnter item number to remove: "))

        # Check if the selected item number is valid
        while num < 1 or num > len(cart_products):

            print("That item does not exist in your cart!")

            num = int(input("Enter item number to remove: "))

        # Get the selected product
        selected_product = cart_products[num - 1]

        # Subtract one from the product quantity
        shopping_cart[selected_product] -= 1

        print("\nRemoved 1 " + selected_product + " from your cart!")

        # If the quantity reaches zero, remove the product from the dictionary
        if shopping_cart[selected_product] == 0:

            shopping_cart.pop(selected_product)
            print(selected_product + " has been removed from your cart.")

        # Otherwise, display the remaining quantity
        else:
            print(selected_product + " quantity is now " + str(shopping_cart[selected_product]) + ".")


# Function to calculate the shopping cart total
def calculate_total(products, shopping_cart):

    total = 0.0

    # Go through each product in the shopping cart
    for product, quantity in shopping_cart.items():

        # Get the product price
        price = products[product]

        # Calculate the total price for that product
        line_total = price * quantity

        # Add the product total to the overall total
        total += line_total

    return total


# Function to display the shopping cart
def display_cart(products, shopping_cart):

    print("\n========== YOUR SHOPPING CART ==========")

    # Check if the shopping cart is empty
    if len(shopping_cart) == 0:
        print("Your shopping cart is empty!")

    else:
        print("\nProduct       Unit Price   Quantity   Line Total")

        total_items = 0

        # Display each product, price, quantity, and line total
        for product, quantity in shopping_cart.items():

            price = products[product]
            line_total = price * quantity
            total_items += quantity

            print(
                product + "       $" + str(price)
                + "          " + str(quantity)
                + "          $" + str(line_total)
            )

        # Calculate and display the subtotal
        subtotal = calculate_total(products, shopping_cart)

        print("\nTotal Items: " + str(total_items))
        print("Subtotal: $" + str(subtotal))


# Function to calculate the discount based on the subtotal
def calculate_discount(total):

    # Give no discount if the total is less than $10
    if total < 10:
        return 0

    # Give a 5% discount if the total is less than $20
    elif total < 20:
        return 5

    # Give a 10% discount if the total is less than $40
    elif total < 40:
        return 10

    # Give a 15% discount if the total is $40 or more
    else:
        return 15


# Function to display the current shopping cart total
def view_total(products, shopping_cart):

    print("\n========== CURRENT TOTAL ==========")

    # Calculate the current subtotal
    total = calculate_total(products, shopping_cart)

    print("Subtotal: $" + str(total))


# Function to print the final receipt
def checkout(products, shopping_cart):

    # Check if the shopping cart is empty
    if len(shopping_cart) == 0:

        print("\nYour shopping cart is empty!")
        print("Please add a product before checking out.")

        return False

    else:

        # Calculate the subtotal, discount, savings, and final total
        subtotal = calculate_total(products, shopping_cart)
        discount_percent = calculate_discount(subtotal)
        amount_saved = subtotal * discount_percent / 100
        final_total = subtotal - amount_saved

        # Get the current date
        today = datetime.now()

        # Display the receipt heading and date
        print("\n========== RECEIPT ==========")
        print("Date: " + today.strftime("%m/%d/%Y"))
        print("\nProduct       Unit Price   Quantity   Line Total")

        total_items = 0

        # Display each product on the receipt
        for product, quantity in shopping_cart.items():

            price = products[product]

            line_total = price * quantity

            total_items += quantity

            print(
                product + "       $" + str(price)
                + "          " + str(quantity)
                + "          $" + str(line_total)
            )

        # Display the final receipt information
        print("\nTotal Items: " + str(total_items))
        print("Subtotal: $" + str(subtotal))
        print("Discount: " + str(discount_percent) + "%")
        print("Amount Saved: $" + str(amount_saved))
        print("Final Total: $" + str(final_total))
        print("\nThank you for shopping!")

        return True


# Main Program

# Create a variable to control when the program ends
finished = False

# Keep displaying the menu until checkout is completed
while finished == False:

    # Display the main menu
    print("\n========== SMART SHOPPING CART ==========")
    print("1. View Available Products")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. View Shopping Cart")
    print("5. View Current Total")
    print("6. Checkout")

    # Ask the user to enter a menu choice
    choice = int(input("\nEnter your choice: "))

    # Check if the menu choice is valid
    while choice < 1 or choice > 6:

        print("Invalid option!")
        choice = int(input("Please choose a number between 1 and 6: "))

    # Run the function that matches the user's choice
    if choice == 1:
        display_products(products)

    elif choice == 2:
        add_product(products, shopping_cart)

    elif choice == 3:
        remove_product(shopping_cart)

    elif choice == 4:
        display_cart(products, shopping_cart)

    elif choice == 5:
        view_total(products, shopping_cart)

    elif choice == 6:

        # End the program if checkout is successful
        if checkout(products, shopping_cart) == True:
            finished = True