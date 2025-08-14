price=input('Enter the original price')
discount_percent=input('Enter the discount')
price=float(price)
#Casting the variable data types
discount_percent=float(discount_percent)
discountpercent=float(discount_percent*0.01)

def calculate_discount(price,discount_percent):
    if(float(discount_percent))>=20:
      discountPrice=float(price-(price*discountpercent))
      return float(discountPrice)
    else:
        return price

print(float(calculate_discount(price,discount_percent)) )
