# Grocery store management system #
items={}
def get_items():
    for i in range(5):
        name=input(f"The item number {i+1} name's :")
        while True:
            try:
                price=float(input(f"Enter the item's price:"))
                if price < 0:
                    print("inavalid price.")
                else:
                    break #to handle non-numeric characters in the price#
            except ValueError:
                print("Invalid Input.Enter an valid price.")
        items[name]=price
    return items  
def calculate_total(items):
    total=0
    for price in items.values():
      total+=price
    print( f"the total price of items is",total) 
    if total > 100 :
       discounted_price = total - (total*0.1)
       print(f" The discounted price (10% Discount)  : {discounted_price}")
    elif  50 <= total <=100 :
       discounted_price = total - (total*0.05)
       print(f" The discounted price (5% Discount)  : {discounted_price}")
    else :
       print(f" No Discount Applied for total price below than 50.")
    return total
def process_purchase():
    dict_items=get_items()
    total_price=calculate_total(items)
    for i, (name, price) in enumerate(items.items(), start=1): #the items method return two values,it you want to return 3 values you can use enumerate() and in thier arguent use items and the start position.#
        print(f"Item Number {i}\n Item's name {name}\n Item's price {price}")
    
def main():
    grocery_items=process_purchase()
    print("Items Informations:",grocery_items)
main()



 

