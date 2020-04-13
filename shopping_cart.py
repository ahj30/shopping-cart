# shopping_cart.py
import datetime

TAX_RATE = .0875 #NYC TAX RATE CONSTANT

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

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes. 
    Param: my_price (numeric, like int or float) the number to be formatted.
    Example: to_usd(4000.444444) 
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71
def find_product(selection, choices):
    """
    Takes the first product from the matching products list to be used in select products list loop.
    Params: selection, str ID matching in the list. choices, list to be drawn from. 
    Example: ID input is 6, and that is a valid ID, return the product from the products list
    """
    matching_products = [p for p in choices if str(p["id"]) == str(selection)]
    matching_product = matching_products[0]
    return matching_product
def receipt_seperator():
    """
    Line that seperates sections on receipt
    """
    print("----------------------------------------")    
def receipt_header():
    """
    Header of receipt that displays store information
    """
    print("----------------------------------------")
    print("            COSTCO WHOLESALE")
    print("             WWW.COSTCO.COM")
    print("             517 E 117TH ST")
    print("           NEW YORK, NY 10035")
    print("----------------------------------------")    
def receipt_footer():
    """
    End of receipt that displays thank you message
    """
    print("----------------------------------------")
    print("THANK YOU FOR SHOPPING COSTCO WHOLESALE!")
    print("----------------------------------------")
def human_friendly_timestamp(current_time):
    """
    Formats the time of checkout to user friendly format.
    Param: current_time, the datetime to be formatted.
    Example: Make 2020-4-1 18:12:13 into 2020-04-01 06:12:13 PM
    """
    return current_time.strftime("%Y-%m-%d %I:%M:%S %p")
def calculate_tax(sub):
    """
    Calculates total tax on the bill.
    Param:sub(numeric, like int or float) the total to be taxed.
    Example: 100 subtotal with .0875 tax is 8.75
    """
    return sub*TAX_RATE
def calculate_subtotal(list):
    """
    Calculates the subtotal of item prices.
    Param:list, a list of the item subtotals.
    Example: item subtotals are 4.50 and 5.25, returns 9.75
    """
    return sum(list)

(product_ids) = [str(p["id"]) for p in products]

sub = [] ### TO STORE ITEM SUBTOTALS
selected_ids = [] ### TO STORE THE IDs

now = datetime.datetime.now()
time = human_friendly_timestamp(now)
###FIRST PROCESS TAKES THE IDs AND STORES THEM IN A LIST
####PRINT "INVALID ENTRY" IF PRODUCT ID NOT MATCHING OR A WORD OTHER THAN "DONE"  

if __name__ == "__main__":
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
receipt_header()
print("CHECKOUT AT: " + time)
receipt_seperator()
print("SELECTED PRODUCTS:")

for selected_identifier in selected_ids:
    matching_product = find_product(selected_identifier,products)   
    print(" ... " + matching_product["name"] + " " + "(" + to_usd(matching_product["price"]) + ")") 
    sub.append(matching_product["price"])

receipt_seperator()
sub_total = calculate_subtotal(sub)
print("SUBTOTAL: " + to_usd(sub_total))
tax = calculate_tax(sub_total)
print("TAX: " + to_usd(tax))
total = sub_total + tax
print("TOTAL: " + to_usd(total))
receipt_footer()
###END