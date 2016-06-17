print("There is good!")
#print(abs(-99))
dreamitem = ["balik","lol"]
shop = str(input("Please enter you dream item: "))
print(shop)
dreamitem.append(shop)
dreamitemprice = [120,134]
shopp = int(input("You dream price:"))
print(shopp)
dreamitemprice.append(shopp)
money = int(input("You have money now?: "))
print(money)
moneygoat = int(input("You more money?: "))
print(moneygoat)
money = money + moneygoat
togoal = shopp - money
print(abs(moneygoat),"goat money on day")
if togoal >= -1:
 print("To goal: ",int(togoal))
else:
 print("Yea.. you have a extra money: ", togoal)
if money >= shopp:
 print("WHOO!!YOU ARE BUY NOW ITEM!!")
else:
 print("Wait more money...")
