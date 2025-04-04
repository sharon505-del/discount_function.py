# Define the function to calculate the discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Directly insert values instead of using input()
price = 100  # Example price of the item
discount_percent = 25  # Example discount percentage

# Call the function and print the result
final_price = calculate_discount(price, discount_percent)

# Display the final price
print(f"The final price after applying the discount is: {final_price}")

