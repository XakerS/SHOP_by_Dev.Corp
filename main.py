print("There is good!")
#print(abs(-99))
shop = str(input("Please enter you dream item: "))
print(shop)
shopp = int(input("You dream price:"))
print(shopp)
money = int(input("You have money now?: "))
print(money)
moneygoat = int(input("You more money?: "))
print(moneygoat)
alprice = []
alprice.append(shopp)
money = money + moneygoat
togoal = shopp - money
print(abs(moneygoat),"goat money on day")
if money == shop:
 print("WHOO!!YOU ARE BUY NOW ITEM!!")
else:
 print("To goal: ",int(togoal))
