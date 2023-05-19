model = int(input("Enter the product type: "))
priceProduct = int(input("Enter the price of the product: "))
if model == 172:
    totalPrice = priceProduct + 0.18
    print("The totalCost is: ", totalPrice)
elif model == 188:
    totalPrice = priceProduct + 0.8
    print("The totalCost is: ", totalPrice)
elif model == 196:
    totalPrice = priceProduct + 0
    print("The totalCost is: ", totalPrice)
else:
    print("Incorrect product")


