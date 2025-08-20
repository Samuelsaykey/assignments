## question 1

# create function named calculate_discount(price, discount_percent)
# funtion calculates final price aftr discount

def calculate_discount(price, discount_percent):
    """This function takes the original price and discount percentage.
    If the discount is 20% or higher, it applies the discount and returns the final price.
    Otherwise, it returns the original price.

    """
    if discount_percent >= 20: #check if discount is 20% or higher
        discount_amount = price * (discount_percent / 100) #calculate discount amount
        final_price = price - discount_amount
        return final_price
    else:
        return price #return original price if discount is less than 20%
    
#question 2
#prompt user to enter the orginal price
price = float(input("enter the original price of the item: "))
 #prompt user to enter the discount percentage
discount_percent = float(input("enter the discount percentage: "))

 #call the function and print the final price
final_price = calculate_discount(price, discount_percent)  

    #the final price after discount is:
if discount_percent >= 20:
        print("The final price after applying discount is:", final_price) 
else:
        print("no discount applied, the final price is:", final_price)
