# shopping_cart.py
from datetime import datetime
import os

from dotenv import load_dotenv

load_dotenv()

#get player's name from .env file
TAX_RATE = os.getenv("TAX_RATE", default=.0875)

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50, "price_per": "item"},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99, "price_per": "item"},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49, "price_per": "item"},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99, "price_per": "item"},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99, "price_per": "item"},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99, "price_per": "item"},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50, "price_per": "item"},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25, "price_per": "item"},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50, "price_per": "item"},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99, "price_per": "item"},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99, "price_per": "item"},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50, "price_per": "item"},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00, "price_per": "item"},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99, "price_per": "item"},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50, "price_per": "item"},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50, "price_per": "item"},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99, "price_per": "item"},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50, "price_per": "item"},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99, "price_per": "item"},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25, "price_per": "item"},
    {"id":21, "name": "Organic Bananas", "department": "fruit", "aisle": "fresh fruit", "price": 0.79, "price_per": "pound"}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# TODO: write some Python code here to produce the desired output

# datetime object containing current date and time
now = datetime.now()

print("-------------------------------------")
print("TIFFANY AND GRO")
print("-------------------------------------")

print("Web: www.tiffanyandgro.com")
print("Phone: 632.495.2827")
print("Checkout Time: " + now.strftime("%Y-%m-%d %H:%M:%S"))


continue_shop = True

product_length = len(products)
shopping_list = []
product_ids = []
for product in products:
    product_ids.append(str(product["id"]))



while continue_shop == True:
    product_id = input("Please input a product identifier, or 'DONE' if there are no more items: ")
    if product_id in product_ids:
        shopping_list.append(int(product_id)) 
    elif product_id == "DONE":
        continue_shop == False
        break
    else:
        print("Hey, are you sure that product identifier is correct? Please try again!")

total_cost = []


print("-------------------------------------")
print("Shoping Cart Items: ")

for item in shopping_list:
    print("+ " + products[item - 1]["name"] + " " + str(to_usd(products[item - 1]["price"])))
    total_cost.append(products[item - 1]["price"])

print("-------------------------------------")

print("Subtotal:", to_usd(sum(total_cost)))
sales_tax = sum(total_cost) * float(TAX_RATE)
print("Plus NYC Sales Tax (" + str(float(TAX_RATE) * 100)+ "%):", to_usd(sales_tax))
total = sales_tax + sum(total_cost)
print("Total: " + str(to_usd(total)))

print("-------------------------------------")
print("Thanks for your business! Please come again.")