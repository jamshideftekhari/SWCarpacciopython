

# 1 - Hello world 
# 2 - input/echo number of items
# 3 - input/echo price of items
# 4 - echo Tax levels Hard coded
# 5 - receive to letter state codes echo and show tax level
# 6 - Calculate price
# 7 - List hard coded discount values
# 8 - calculate discount value based on order value
# 9 - calculate total price with discount included. 
# 10 - add tax levels to file/DB
# 11 - add discount values to file/DB






from StatesTax import StatesTax
from Discount import Discount
from Calculator import Calculator
# 1 - Hello world 
print("********Welcome to state price calculator************")

# 2 - input/echo number of items
itemnr = int(input("Please enter the number of items yo want to buy -> "))
print("You entered: " + str(itemnr))


# 3 - input/echo price of items
price = int(input("please enter the price of the item you buy -> "))
print("you entered: "+ str(price))

# 4 - echo Tax levels Hard coded
print ("List of states:")
for st in StatesTax:
    print(st.value)

# 5 - receive to letter state codes echo and show tax level
stateKode = input("enter 2 cifer state code from the list -> ")
print("you entered: " + stateKode)
Cal = Calculator()
taxparameters = Cal.getTaxValue(stateKode)
print("Tax Rate: " + str(taxparameters.value[2]))
#st = StatesTax
#print(st)
#print(st.UT.value)
#print(st.UT.value[0])

# 6 - Calculate price 
print("total price: " )
price = Cal.calculteprice(price, itemnr, taxparameters.value[2])
print(str(price))

# 7 - List hard coded discount values
print("discont levels: (number of items, Discount% )")
for dis in Discount:
    print(dis.value)

# 8 - calculate discount value based on order value 
Cal.getDiscountValue(900)
Cal.getDiscountValue(1900)
Cal.getDiscountValue(5900)
Cal.getDiscountValue(10900)
Cal.getDiscountValue(50900)

# 9 - calculate total price with discount included. 

# 10 - add tax levels to file/DB

# 11 - add discount values to file/DB