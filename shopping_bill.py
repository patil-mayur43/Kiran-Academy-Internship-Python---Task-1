
def calculateElectronicsGST(a, b):
    return (a + b) * 1.18


def calculateFashionGST(c, d):
    return (c + d) * 1.13


def calculateFoodGST(e):
    return e * 1.07


def totalBill(a, b, c, d, e):
    return (
        calculateElectronicsGST(a, b)
        + calculateFashionGST(c, d)
        + calculateFoodGST(e)
    )


def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 0.20
    return total - discount


# Sample values
a, b, c, d, e = 100, 100, 100, 100, 100

# Before GST prices
electronics_before = a + b
fashion_before = c + d
food_before = e

# After GST prices
electronics_after = calculateElectronicsGST(a, b)
fashion_after = calculateFashionGST(c, d)
food_after = calculateFoodGST(e)

# Total and discount
total = totalBill(a, b, c, d, e)
discount = total * 0.20
final_amount = calculateDiscountedBill(a, b, c, d, e)

# Display bill
print("========== SHOPPING BILL ==========")

print("\nElectronics:")
print(f"Before GST: ₹{electronics_before:.2f}")
print(f"After GST (18%): ₹{electronics_after:.2f}")

print("\nFashion:")
print(f"Before GST: ₹{fashion_before:.2f}")
print(f"After GST (13%): ₹{fashion_after:.2f}")

print("\nFood:")
print(f"Before GST: ₹{food_before:.2f}")
print(f"After GST (7%): ₹{food_after:.2f}")

print("\n========== FINAL SUMMARY ==========")
print(f"Total before GST: ₹{electronics_before + fashion_before + food_before:.2f}")
print(f"Total after GST: ₹{total:.2f}")
print(f"Discount (20%): ₹{discount:.2f}")
print(f"Final payable amount: ₹{final_amount:.2f}")
print("===================================")
