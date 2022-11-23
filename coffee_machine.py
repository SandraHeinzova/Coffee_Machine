from source_data import MENU
from source_data import resources
from coffee_machine_logo import logo
from coffee_machine_logo import coffee
import os
import time

# kontrola ingrediencí
def check_ingredients(drink):
    if (MENU[drink]['ingredients']['water']) <= resources['water']:
        if (MENU[drink]['ingredients']['milk']) <= resources['milk']:
            if (MENU[drink]['ingredients']['coffee']) <= resources['coffee']:
                print("There is enough ingredients to make your drink.")
                resources['water'] -= (MENU[drink]['ingredients']['water'])
                resources['milk'] -= (MENU[drink]['ingredients']['milk'])
                resources['coffee'] -= (MENU[drink]['ingredients']['coffee'])
                return True
            else:
                print("Unfortunately, there is not enough ingredients to make your drink.")
                return False
        else:
            print("Unfortunately, there is not enough ingredients to make your drink.")   
            return False
    else:
        print("Unfortunately, there is not enough ingredients to make your drink.")
        return False
        

def payment(drink):
    print ("Please insert your coins. Coffee machine accepts 1CZK, 2CZK, 5CZK, 10CZK, 20CZK, 50CZK.")
    payment_1 = int(input("How many 1CZK will you insert?: "))
    payment_2 = int(input("How many 2CZK will you insert?: "))
    payment_5 = int(input("How many 5CZK will you insert?: "))
    payment_10 = int(input("How many 10CZK will you insert?: "))
    payment_20 = int(input("How many 20CZK will you insert?: "))
    payment_50 = int(input("How many 50CZK will you insert?: "))
    
    totall = int(payment_1*1 + payment_2*2 + payment_5*5 + payment_10*10 + payment_20*20 + payment_50*50)
    
    print("-" * 50) 
    print(f"You inserted {totall}CZK in totall.")
    print(f"The {drink} costs {MENU [drink]['cost']} CZK")
    
    if totall > MENU[drink]['cost']:
        print(f"Here is your money back - {totall - MENU [drink]['cost']}CZK")
        return True
    elif totall < MENU [drink]['cost']:
        print("You did not insert enough money to pay for your drink.")
        print("-" * 50) 
        payment(drink)
        return True
    else:
        print("Your payment was accutate, thank you.")
        return True
    
    
    

def coffee_machine():
    print (logo)
    while True:
        drink = input("What coffee would you like to order? (espresso/latte/cappuccino). \nTo turn off the coffee machine type 'end'.\nTo check remaining ingredients type 'report.\n").lower()     
        print("-" * 50)   
        try:
            if drink == "report":
                print(f"Water: {resources['water']}")
                print(f"Milk: {resources['milk']}")
                print(f"Coffee: {resources['coffee']}")
                print("-" * 50) 
                
            elif drink == "end":
                print("Coffe machine will be turned off in 5 seconds. Thank you for using our coffee machine.\nHave a nice day!")
                time.sleep(5)
                os.system("cls")
                break
            elif drink == drink:
                if check_ingredients(drink) == True:
                    if payment(drink) == True:
                        print("Your drink is being prepared.")
                        print(coffee)
                        
                else: 
                    print("Thank you for using our coffee machine. We will refill resources soon.\nHave a nice day.")
                    time.sleep(10)
                    os.system("cls")
                    break           
        except KeyError:
                print("I do not understand your choice. ")
                print("-" * 50) 
                
    
coffee_machine()

       