from source_data import MENU
from source_data import resources

# ceny nápojů
espresso_price = MENU ['espresso']['cost']
latte_price = MENU ['latte']['cost']
cappuccino_price = MENU ['cappuccino']['cost']


# kontrola ingrediencí
def check_ingredients(drink):
    if (MENU[drink]['ingredients']['water']) <= resources['water']:
        if (MENU[drink]['ingredients']['milk']) <= resources['milk']:
            if (MENU[drink]['ingredients']['coffee']) <= resources['coffee']:
                print("Na Váš nápoj máme dostatek ingrediencí")
                resources['water'] -= (MENU[drink]['ingredients']['water'])
                resources['milk'] -= (MENU[drink]['ingredients']['milk'])
                resources['coffee'] -= (MENU[drink]['ingredients']['coffee'])
                return True
            else:
                print("Na Váš nápoj bohužel nemáme dostatek ingrediencí.")
                return False
        else:
            print("Na Váš nápoj bohužel nemáme dostatek ingrediencí.")   
            return False
    else:
        print("Na Váš nápoj bohužel nemáme dostatek ingrediencí.")
        return False
        

def payment(drink):
    print ("Prosím, vložte mince 1, 2, 5, 10, 20, 50")
    payment_1 = int(input("Kolik 1Kč chcete vložit?: "))
    payment_2 = int(input("Kolik 2Kč chcete vložit?: "))
    payment_5 = int(input("Kolik 5Kč chcete vložit?: "))
    payment_10 = int(input("Kolik 10Kč chcete vložit?: "))
    payment_20 = int(input("Kolik 20Kč chcete vložit?: "))
    payment_50 = int(input("Kolik 50Kč chcete vložit?: "))
    
    totall = int(payment_1*1 + payment_2*2 + payment_5*5 + payment_10*10 + payment_20*20 + payment_50*50)
    
    print(f"Celkem jste vložili {totall}Kč")
    print(f"Cena {drink} je {MENU [drink]['cost']}")
    
    if totall > MENU[drink]['cost']:
        print(f"Zde máte nazpět {totall - MENU [drink]['cost']}Kč")
        return True
    elif totall < MENU [drink]['cost']:
        print("Nevložili jste dostatek k zaplacení Vašeho nápoje.")
    else:
        print("Platba byla přesná, děkujeme.")
    
    
    

def coffee_machine():
    while True:
        drink = input("Co byste si dal? (espresso/latte/cappuccino): ")        
        try:
            if drink == "report":
                print(f"Voda: {resources['water']}")
                print(f"Mléko: {resources['milk']}")
                print(f"Káva: {resources['coffee']}")
            elif drink == drink:
                if check_ingredients(drink) == True:
                    if payment(drink) == True:
                        print("Váš nápoj se připravuje.")
                else: 
                    print("Děkujeme, že jste využil tento automat na kávu. Brzy doplníme zásoby.")
                    break           
        except KeyError:
                print("Nerozumím Vaší volbě. ")
    
coffee_machine()

       