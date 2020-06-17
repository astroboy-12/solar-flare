# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 23:29:06 2020

@author: adarsh
"""

# Write your code here

print('Starting to make a coffee')
print('Grinding coffee beans')
print('Boiling water')
print('Mixing boiled water with crushed coffee beans')
print('Pouring coffee into the cup')
print('Pouring some milk into the cup')
print('Coffee is ready!')



def coffee_printing(s):
    money = 550
    water = 400
    milk = 540
    beans = 120
    cups = 9
    while(s!=exit):
        while(s!='exit'):
            if s=='buy':
                s1 = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
                if s1=='1':
                    if water<250:
                        print('Sorry, not enough water!')
                        break
                    if beans<16:
                        print('Sorry, not enough coffee beans!')
                        break       
                    print('I have enough resources, making you a coffee!')
                    money = money + 4
                    beans = beans - 16
                    water = water - 250
                    cups = cups-1
                    break
                elif s1=='2':
                    if water<350:
                        print('Sorry, not enough water!')
                        break
                    if beans<20:
                        print('Sorry, not enough coffee beans!')
                        break  
                    if milk<75:
                        print('Sorry, not enough milk!')
                        break     
                    print('I have enough resources, making you a coffee!')
                    money = money + 7
                    beans = beans - 20
                    water = water - 350
                    milk = milk -75
                    cups = cups-1
                    break
                elif s1 == '3':
                    if water<200:
                        print('Sorry, not enough water!')
                        break
                    if beans<12:
                        print('Sorry, not enough coffee beans!')
                        break
                    if milk<100:
                        print('Sorry, not enough milk!')
                        break          
                    print('I have enough resources, making you a coffee!')
                    money = money + 6
                    beans = beans - 12
                    water = water - 200
                    milk = milk -100
                    cups = cups-1
                    break
                else:
                    break
            elif s=='fill':
                a1 = int(input('Write how many ml of water do you want to add:'))
                a2 = int(input('Write how many ml of milk do you want to add:'))
                a3 = int(input('Write how many grams of coffee beans do you want to add:'))
                a4 = int(input('Write how many disposable cups of coffee do you want to add:'))
                beans = beans + a3
                water = water +a1
                milk = milk +a2
                cups = cups+a4
                break
            elif s=='take':
                print('I gave you ${}'.format(money))
                money = 0
                break
            elif s=='remaining':
                print('The coffee machine has:')
                print('{} of water'.format(water))
                print('{} of milk'.format(milk))
                print('{} of coffee beans'.format(beans))
                print('{} of disposable cups'.format(cups))
                print('{} of money'.format(money))
                break
        if s=='exit':
            return
        s = input('Write action (buy, fill, take, remaining, exit):')
s = input('Write action (buy, fill, take, remaining, exit):')
coffee_printing(s)

        
        
