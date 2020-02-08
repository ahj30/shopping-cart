# shopping_cart.py

#from pprint import pprint

import datetime




products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017



product_ids = [ str(p["id"]) for p in products ]



#print(products)
# pprint(products)

# TODO: write some Python code here to produce the desired output

### ALLOWS PRICE TO BE CONVERETED TO CURRENCY FORMAT

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes. 
    Example: to_usd(4000.444444) 
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

### INPUT USER INFO

sub_total = 0
selected_ids = [] ### TO STORE THE IDs




###FIRST PROCESS TAKES THE IDs AND STORES THEM IN A LIST
####PRINT INVALID ENTRY IF PRODUCT ID NOT MATCHING OR A WORD OTHER THAN "DONE"  


while True:
    selected_identifier = input("Please input a product identifier, or type 'DONE': ")
    selected_identifier = selected_identifier.upper()       #PRODUCT IDS UNAFFECTED BY UPPERCASE
    if selected_identifier == "DONE":
        break
    else:
        if selected_identifier in product_ids:
            selected_ids.append(selected_identifier)
        else:
            print("INVALID ENTRY") 
  

###SECOND PROCESS LISTS OUT THE ITEMS AND PRICES USING THE SELECTED IDs LIST

now = datetime.datetime.now()

print("----------------------------------------")
print("            COSTCO WHOLESALE")
print("             WWW.COSTCO.COM")
print("           PENTAGON CITY #233")
print("           1200 S FERN STREET")
print("           ARLINGTON,VA 22202")
print("----------------------------------------")
print("CHECKOUT AT: " + now.strftime("%Y-%m-%d %I:%M:%S %p"))
print("----------------------------------------")
print("SELECTED PRODUCTS:")

for selected_identifier in selected_ids:
    matching_products = [p for p in products if str(p["id"]) == str(selected_identifier)]
    matching_product = matching_products[0]
    sub_total = sub_total + matching_product["price"]    
    print(" ... " + matching_product["name"] + " " + "(" + to_usd(matching_product["price"]) + ")") 

print("----------------------------------------")

print("SUBTOTAL: " + to_usd(sub_total))

tax = sub_total * .0875 #NYC Sales tax

print("TAX: " + to_usd(tax))

total = sub_total + tax

print("TOTAL: " + to_usd(total))

print("----------------------------------------")
print("THANK YOU FOR SHOPPING COSTCO WHOLESALE!")
print("----------------------------------------")