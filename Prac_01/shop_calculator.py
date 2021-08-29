

total_price = 0
number_items = int(input(" enter number of items: "))
if number_items <=0:
    print("Invalid number of items!")
else:
    for i in range(1, number_items+1):
        item_price = float(input("Enter item price:"))
        total_price = total_price + item_price
    print(total_price)
    print("total price with discount: ",total_price - (total_price*10)/100)
















#first_price_item = int(input("please enter the item price"))
#second_price_item = int(input("please enter the item price"))
#third_price_item = int(input("please enter the item price"))

#total_price_item = first_price_item + second_price_item + third_price_item
#print (total_price_item)

