# shopping_cart.py
from datetime import datetime
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from dotenv import load_dotenv

load_dotenv()

#BONUS: CONFIGURING SALES TAX RATE
#get tax rate name from .env file
TAX_RATE = os.getenv("TAX_RATE", default=.0875)

#list of products and descriptions
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


#to convert numbers to price format
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71



#datetime object containing current date and time
now = datetime.now()


#boolean to keep track of whether to continue prompting user to input items or not
continue_shop = True

#find the length of the list of products
product_length = len(products)
#initialize list to hold user entered product ids
shopping_list = []
#initialize list to hold all existing product ids in string format
product_ids = []

#add product ids in string format to a list
for product in products:
    product_ids.append(str(product["id"]))

#initialize list for emailing the receipt
receipt_list = []
#initialize list for adding items to be printed onto a txt file
items_bought = []
#initialize list to hold items that are pay per pound
pounds = []

#loop and ask user to input product id until user is done
while continue_shop == True:
    product_id = input("Please input a product identifier, or 'DONE' if there are no more items: ")
    if product_id in product_ids:
        shopping_list.append(int(product_id)) 
        #for emailing the receipt
        receipt_list.append({"id":int(product_id), "name": products[int(product_id)-1]["name"], "price": to_usd(products[int(product_id)-1]["price"])})
        #for printing the receipt
        items_bought.append(products[int(product_id) - 1]["name"])
        #if the item is priced in pounds, ask user to enter number of pounds, store the number of pounds
        if products[int(product_id) - 1]["price_per"] == "pound":
            pounds_amount = float(input("Please enter the number of pounds: "))
            pounds.append(pounds_amount)
        else:
            pounds.append(0)
    #leave loop when user is finished
    elif product_id == "DONE":
        continue_shop = False
    #if user inputs invalid input, tell user to try again
    else:
        print("Hey, are you sure that product identifier is correct? Please try again!")


#count the number of items bought by user
number_of_items = len(items_bought)

#print introduction
print("-------------------------------------")
print("TIFFANY AND GRO")
print("-------------------------------------")

print("Web: www.tiffanyandgro.com")
print("Phone: 632.495.2827")
print("Checkout Time: " + now.strftime("%Y-%m-%d %H:%M:%S"))

print("-------------------------------------")
print("Shopping Cart Items: ")

#list to add the prices of items
total_cost = []

count = 0
#loop through each item that the user has bought and find the price
for item in shopping_list:
    count = count + 1
    #if the product is priced by pound
    #BONUS: HANDLING PRICE PER POUND
    if products[item - 1]["price_per"] == "pound":
        price = products[item - 1]["price"] * pounds[count-1]
        print_item = ("+ " + products[item - 1]["name"] + " " + str(to_usd(price)))
        print(print_item)
        total_cost.append(price)
    else:
        print("+ " + products[item - 1]["name"] + " " + str(to_usd(products[item - 1]["price"])))
        total_cost.append(products[item - 1]["price"])

print("-------------------------------------")

#print totals and tax amounts
print("Subtotal:", to_usd(sum(total_cost)))
sales_tax = sum(total_cost) * float(TAX_RATE)
print("Plus NYC Sales Tax (" + str(float(TAX_RATE) * 100)+ "%):", to_usd(sales_tax))
total = sales_tax + sum(total_cost)
print("Total: " + str(to_usd(total)))

#print farewell message
print("-------------------------------------")
print("Thanks for your business! Please come again.")

#BONUS: SENDING RECEIPTS VIA EMAIL
#boolean to ask user if they want receipt emailed
email = True

while email == True: 
    send_email = input("Would you like to receive a receipt via email? Enter 'YES' or 'NO': ")
    #send email to user through sendgrid
    if send_email == "YES":
        user_address = input("Enter your email address: ")
        SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
        SENDGRID_TEMPLATE_ID = os.getenv("SENDGRID_TEMPLATE_ID", default="OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'")
        SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")

        # this must match the test data structure
        template_data = {
            "total_price_usd": str(to_usd(total)),
            "human_friendly_timestamp": now.strftime("%Y-%m-%d %H:%M:%S"),
            "products": receipt_list
        } # or construct this dictionary dynamically based on the results of some other process :-D

        client = SendGridAPIClient(SENDGRID_API_KEY)


        message = Mail(from_email=SENDER_ADDRESS, to_emails=user_address)
        message.template_id = SENDGRID_TEMPLATE_ID
        message.dynamic_template_data = template_data


        try:
            response = client.send(message)
            print("Your receipt has been sent to your email!")
            email = False
        #if the user does not enter a valid email, loop through the loop again
        except Exception as err:
            print("Please enter a valid email.")

    #if the user does not want an email, print farewell  
    elif send_email == "NO":
        email = False
        print("Thank you!")
        break
    #if the user does not enter YES or NO, prompt to try again
    else:
        print("Hey, are you sure you entered correctly? Please try again!")

#BONUS: WRITING RECEIPTS TO FILE
#change directories to the receipts directory within the repository
os.chdir("/Users/tiffanyku/Desktop/shopping-cart/receipts")

#add a file name of the current date and time
file_name = (now.strftime("%Y-%m-%d-%H-%M-%S") + str(now.microsecond) + ".txt")

#open the new txt file and write receipt contents into it
with open(file_name, "w") as file:
    file.write("-------------------------------------")
    file.write("\n")
    file.write("TIFFANY AND GRO")
    file.write("\n")
    file.write("-------------------------------------")
    file.write("\n")    
    file.write("Web: www.tiffanyandgro.com")
    file.write("\n")
    file.write("Phone: 632.495.2827")
    file.write("\n")
    file.write("Checkout Time: " + now.strftime("%Y-%m-%d %H:%M:%S"))
    file.write("\n")
    file.write("-------------------------------------")
    file.write("\n")
    file.write("Shopping Cart Items: ")
    file.write("\n")
    for item in range(0, number_of_items):
        file.write(items_bought[item] + " ")
        file.write(str(to_usd(total_cost[item])))
        file.write("\n")
    file.write("-------------------------------------")
    file.write("\n")
    file.write("Subtotal: " + str(to_usd(sum(total_cost))))
    file.write("\n")
    file.write("Plus NYC Sales Tax (" + str(float(TAX_RATE) * 100)+ "%): " + str(to_usd(sales_tax)))
    file.write("\n")
    file.write("Total: " + str(to_usd(total)))
    file.write("\n")
    file.write("-------------------------------------")
    file.write("\n")
    file.write("Thanks for your business! Please come again.")
