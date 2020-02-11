# Shopping-cart Project


## Installation
Fork this repository, then clone it to download it locally onto your computer.
Choose a familiar download location like the Desktop.

After cloning the repository, navigate there from the command line:

```sh
cd ~/"Your download location"/shopping-cart
```
### Environment Setup
Create and activate a new Anaconda virtual environment:
```sh
conda create -n shopping-env python=3.7 # (first time only)
conda activate shopping-env
```

#### Usage 
To run the program:

```sh
python shopping_cart.py
```

##### Example Output
```sh
(shopping-env)
"USER NAME" ~/Desktop/shopping-cart (master)
$ python shopping_cart.py
Please input a product identifier, or type 'DONE': 1
Please input a product identifier, or type 'DONE': 2
Please input a product identifier, or type 'DONE': 3
Please input a product identifier, or type 'DONE': 4
Please input a product identifier, or type 'DONE': 5
Please input a product identifier, or type 'DONE': 2
Please input a product identifier, or type 'DONE': 2
Please input a product identifier, or type 'DONE': 10
Please input a product identifier, or type 'DONE': DONE
#----------------------------------------
#            COSTCO WHOLESALE
#             WWW.COSTCO.COM
#             517 E 117TH ST
#           NEW YORK, NY 10035
#----------------------------------------
#CHECKOUT AT: 2020-02-10 07:11:57 PM
#----------------------------------------
#SELECTED PRODUCTS:
# ... Chocolate Sandwich Cookies ($3.50)
# ... All-Seasons Salt ($4.99)
# ... Robust Golden Unsweetened Oolong Tea ($2.49)
# ... Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce ($6.99)
# ... Green Chile Anytime Sauce ($7.99)
# ... All-Seasons Salt ($4.99)
# ... All-Seasons Salt ($4.99)
# ... Sparkling Orange Juice & Prickly Pear Beverage ($2.99)
#----------------------------------------
#SUBTOTAL: $38.93
#TAX: $3.41
#TOTAL: $42.34
#----------------------------------------
#THANK YOU FOR SHOPPING COSTCO WHOLESALE!
#----------------------------------------
```

