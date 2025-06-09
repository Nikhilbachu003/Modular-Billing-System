from datetime import datetime

def take_order(Menuu):
    cart = []
    while True:
        try:
            item_id = int(input("Enter item ID to add to cart (0 to finish): "))
            if item_id == 0:
                break
            item = Menuu.get_item_by_id(item_id)
            if not item:
                print("Invalid item ID. Try again.")
                continue
            quantity = int(input(f"Enter quantity for {item[0]}: "))
            cart.append((item_id, item[0], item[1], quantity))
        except ValueError:
            print("Invalid input. Please enter numbers.")                   
    return cart

def generate_bill(cart):
    if cart:
        print("\n" + "-" * 60)
        print(" " * 20 + "BILL")
        print("-" * 60)
        print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 60)
        print(f"{'ITEM NAME':<20}{'QUANTITY':<15}{'PRICE':<10}")
        print("-" * 60)

        total = 0
        for item_id, name, price, qty in cart:
            item_total = price * qty
            total += item_total
            print(f"{name:<20}{qty:<15}{'₹' + format(item_total, '.2f'):<10}")

        print("-" * 60)
        print(f"{'Total Amount:':<35}{'₹' + format(total, '.2f'):<10}")
        print("-" * 60)
        print("Thank you for visiting! Please come again.".center(60))
        print("-" * 60)
    else:
        print("No items in cart.")
