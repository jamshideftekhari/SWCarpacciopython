from logging import NullHandler
import re
from StatesTax import StatesTax
from Discount import Discount
class Calculator (object):
    st = StatesTax
    dis = Discount
    def __init__(self):
        print ("calculator object initialised ") 
        

    def getTaxValue(self, state):
        for s in self.st:
            if s.value[0] == state.upper():
                print("Record found: ")
                print(s.value)
                return s
            
        print("not found") 
        return s.NOTFound    
           

    def calculteprice(self, price, number, statetax):
        return price*number+price*number*(statetax/100)

    def getDiscountValue(self, number):

        for d in self.dis:
            if number<d.value[0]:
                print("discout tuple found:")
                print(d.value)
                return d
            
        print("no discount")
        