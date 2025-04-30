def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return (discount_percent / 100) * price
    else:
        return price

print(calculate_discount(int(input("Enter the price: ")), int(input("Enter the discount percent: "))))
