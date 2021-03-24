number_of_items = int(input("Number of items: "))

while(number_of_items < 0):
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

running_total = 0

for i in range (0, number_of_items, 1):
    item_cost = float(input("Price of item: "))
    running_total = running_total + item_cost

if running_total > 100:
    running_total = running_total * 0.9

print(f"Total price for {number_of_items} items is ${running_total:.2f}")