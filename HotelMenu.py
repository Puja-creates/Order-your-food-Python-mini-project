#Define the menu of a restaurant
menu = {
    'Pizza' : 500,
    'Pasta' : 400,
    'Burger' : 350,
    'Coffee' : 250,
    'Salad' : 300,
}
print(menu)

#Greet the customer

print("Welcome to Paa Pasta Restaurant!!!!")

print(" Pizza: Rs500\n Pasta: Rs400\n Burger: Rs350\n Coffee: Rs250\n Salad: Rs300")

order_total = 0
# For ex 500+400 = 900 will be displayed in order_total

# Creating another variable so take input from the customer
item_1 = input("Please enter what you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]                #+= The value of right operand is added to the left operand
    print(f"Your Item {item_1} has been added to your order")
else:
    print(f"{item_1} is not available.")

another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "Yes" :
    item_2 = input("Please enter next item: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your Item {item_2} has been added to your order")
    else:
        print(f"{item_2} is not available.")
print(f"Your total order amount is {order_total}")