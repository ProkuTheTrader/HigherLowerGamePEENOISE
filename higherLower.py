import os
clear = lambda: os.system('cls')
import random


logo = """ 
    __  ___       __                 __                              
   / / / (_)___ _/ /_  ___  _____   / /  ____ _      _____  _____    
  / /_/ / / __ `/ __ \/ _ \/ ___/  / /  / __ \ | /| / / _ \/ ___/    
 / __  / / /_/ / / / /  __/ /     / /__/ /_/ / |/ |/ /  __/ /        
/_/ /_/_/\__, /_/ /_/\___/_/     /_____|____/|__/|__/\___/_/         
        /____/                                                                                                                        
"""

vsLogo = """
 _    _______    
| |  / / ___/    
| | / /\__ \     
| |/ /___/ /     
|___//____/      
             
"""


namesAndFollowers = {
    "sy siblings, SM": 16, 
    "manny villar, Housing": 6,
    "enrique razon, Restaurant": 5, 
    "lance gokongwei, Robina": 4,
    "jaime ayala, Ayala": 3,
    "dennis uy, Petrol": 2,
    "tony caktiong, Jollibee": 1,
    
}

tuloyLang = True
points = 0

while tuloyLang == True:
    print(logo)

    def randomPerson(dictionary):
        return random.choice(list(dictionary))
        
    personA = randomPerson(namesAndFollowers)
    personB = randomPerson(namesAndFollowers)

    if personA == personB:
        personA = randomPerson(namesAndFollowers)

    compareA = print(f"Compare A: {personA}")
    print(vsLogo)
    compareB = print(f"Against B: {personB}")
    print(f"Your number of points are: {points}")

    keyOne = namesAndFollowers[personA]
    keyTwo = namesAndFollowers[personB]

    rightAnswer = []

    if keyOne > keyTwo:
        rightAnswer = "a"
    if keyTwo > keyOne:
        rightAnswer = "b"



    aOrB = input(f"Who has more NetWorth? Type 'a' or 'b': ")

    clear()

    if aOrB == rightAnswer:
        print("You Won, You fcking dickhead")
        tuloyLang = True
        points += 1
        print(f"Your number of points are: {points}")
    else:
        print("luh gago, talo ka tanga")
        tuloyLang = False
