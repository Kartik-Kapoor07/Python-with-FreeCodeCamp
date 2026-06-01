#docstring are just like the comments but they are used to describe the purpose of the function and unlike comments they are not ignored by the interpreter and they are stored as an attribute of the function and can be accessed using the __doc__ attribute of the function.

def taxsystem(price_of_item,quantity,tax_rate):
    """
    This function calculates the total price of an item including tax.
    
    Parameters:
    price_of_item (float): The price of a single item.
    quantity (int): The number of items being purchased.
    tax_rate (float): The tax rate as a percentage (e.g., 5 for 5%).
    
    Returns:
    float: The total price including tax.
    """
    total_price = price_of_item * quantity
    tax_amount = total_price * (tax_rate / 100)
    total_price_including_tax = total_price + tax_amount
    return total_price_including_tax

print(taxsystem(100, 15, 5.4))  # Example usage
print("\n")
help(taxsystem)  # This will display the docstring of the function
print("\n")
print(taxsystem.__doc__)  # This will also display the docstring of the function