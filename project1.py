menu = {
    'pizza':40,
    'pasta':50,
    'burger':80,
    'salad':40,
    'coffee':85,
    'soups'  :40,

}

# greeting
print("Welcome to python restaurant")
print("Menu:- pizza: Rs40/npasta: Rs50/nburger: Rs80/nsalad: Rs40/ncoffee: Rs85/nsoups:Rs40")

order_total = 0
#50+30=80

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1] #0+50
    print("your item {item_1}has been added to your order")
else:
    print(f"ordered item {item_1} is not available yet!")
another_order  = input("Do you want to add another item? (Yes/No)")
if another_order == "yes":
    item_2 = input("Enter the second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
         print(f"Ordered item{item_2} is not available!")
print(f"The total amount of items is to pay  {order_total}")
another_order = input("Do you want to add another item? (yes/No)")
if another_order == "yes":
    item_3 = input("Enter the second item = ")
    if item_3 in menu:
        order_total += menu[item_3]
        print(f"Item {item_3} has been added to order")
    else:
         print(f"Ordered item{item_3} is not available!")
print(f"The total amount of items is to pay  {order_total}")

