water_supply = int(input('Write how many ml of water the coffee machine has:')) // 200
milk_supply = int(input('Write how many ml of milk the coffe machine has:')) // 50
coffee_supply = int(input('Write how many grams of coffee beans the coffee machine has:')) // 15

coffee_cups_order = int(input('Write how many cups of coffee you will need:'))

#find how many cups you can make with water in machine
#find how many cups you can make with milk in machine
#find how many cups you can make with coffee in machine(the minimum number between the three variables)
coffee_in_machine = min(water_supply, milk_supply, coffee_supply)

if coffee_cups_order == coffee_in_machine:
    print('Yes, I can make that amount of coffee')
elif coffee_in_machine > coffee_cups_order:
    print('Yes, I can make that amount of coffee (and even', coffee_in_machine - coffee_cups_order, 'more than that)')
else:
    print('No, I can make only', coffee_in_machine, 'cups of coffee')


