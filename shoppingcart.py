# Create a shopping cart programme that willask the user for a food product and the price of that product
# Have an exit clause if the user wishes to stop adding more itemsto their cart
# At the end show th food items and total cost to the usr


foods = []
prices = []
total = 0 

while True:
    food = input("Enter a food to buy or press q to quit: ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter price of the {food}: R"))
        foods.append(food)
        prices.append(price)
        
print("----- YOUR CART -----")

for food in foods:
    print(food, end= " ")
    
for price in prices:
    total += price
    
    
print("/n")
print(f"Your total is: R{total}")