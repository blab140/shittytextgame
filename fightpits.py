import time
import random

def print_pause(lines):
    for (line, pause) in lines:
            print(line)
            time.sleep(pause)
            
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print("WELCOME TO THE FIGHT PITS")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")

time.sleep(3)

bosscounter = 0
monster_int = 0
alive = True

typeplaceint = int(random.randint(1,12))
typeplacelist = ["zero", "slums", "sewers", "country", "suburbs", "bay", "ghetto", "intercity", "pits", "forest", "boroughs", "outposts", "meadows"]
typeplace = typeplacelist[typeplaceint]


placelist = ["zero", "London", "Detroit", "New York", "Tristram", "Toronto", "Emerald City", "Cloud City", "Lordram", "Eidengarde", "Blizzcon 2017", "Waterloo"]
placeint = int(random.randint(1,(len(placelist)-1)))
place = placelist[placeint]              
print_pause([
        ("You are a fighter.", 1.5),
        ("You have always been a fighter...", 1.5)
        ])
print("You grew up in the",typeplace,"of",place)
time.sleep(2)
print_pause([
        ("Now you arrive here, this arena of fortitude, cursed to battle or be worthless.", 3),
        ("You've spent days preparing for this day.", 3),
        ("You prepare to enter the arena and are presented with a choice of weapon", 3)   
        ])
WEAPONS = [('fists', 4, 6, 5), ('barehands', 1, 4, 5), ('shank', 2, 4, 6), ('butcherknife', 3, 8, 6), ('flail', 1, 9, 5), ('shortsword', 2, 5, 6), ('katana', 0, 11, 7)]
#name, attack min, attack max, accuracy
ENEMIES = [('none', 0, 0, 0, 0, 0), ('giant spider', 0, 4, 4, 4, 50), ('troll', 0, 5, 3, 7, 100)]
#name, attack min, attack max, accuracy, health, gold dropped
player = [WEAPONS[1], 20, 20, 0, 0]
#weapon health healthmax gold wins
BOSSES = [('Wyvern', 2, 4, 7, 30, 1000, 2, 1),]
#name, attack min, attack max, accuracy, health, gold dropped, boss factor(stat increases on the new boss append), player accuracy multiplier
monster = [ENEMIES[0]]
def reroll_weapon():
    return int(random.randint(2, (len(WEAPONS)-1)))
def monsterchoice():
        global monster_int
        monster_int = int(random.randint(1, (len(ENEMIES)-1)))
        monster[0] = ENEMIES[monster_int]
def rerollweapon1():
    weapon1_int = int(random.randint(2, (len(WEAPONS)-1)))
def rerollweapon2():
    weapon2_int = int(random.randint(2, (len(WEAPONS)-1)))
def rerollweapon3():
    weapon3_int = int(random.randint(2, (len(WEAPONS)-1)))
def weaponchoice():
    weapon1_int = int(random.randint(2, (len(WEAPONS)-1)))
    while WEAPONS[weapon1_int] == player[0]:
        weapon1_int = reroll_weapon()
    weapon1 = WEAPONS[weapon1_int]
    weapon2_int = int(random.randint(2, (len(WEAPONS)-1)))
    while weapon2_int == weapon1_int:
        weapon2_int = reroll_weapon()
    weapon2 = WEAPONS[weapon2_int]
    weapon3_int = int(random.randint(2, (len(WEAPONS)-1)))
    while weapon3_int == weapon2_int or weapon3_int == weapon1_int:
        weapon3_int = reroll_weapon()
    weapon3 = WEAPONS[weapon3_int]
    print("Please choose 1-5")
    print("1 Drop everything and charge in")
    print('2', weapon1[0])
    print('3', weapon2[0])
    print('4', weapon3[0])
    print('5 stick with your', player[0][0])
    weaponchoice = str(input())
    if weaponchoice == '1':
        print("You feel your rage empower you and you enter the arena unarmed, regardless of the outcome you are sure to gain more money for this feat.")
        time.sleep(3)
        player[0] = WEAPONS[0]
        goldreward_int = int(random.randint(25, 100))
        player[2] = player[2] + goldreward_int
    elif weaponchoice == '2':
        print("You equip the ", weapon1[0])
        player[0] = weapon1
    elif weaponchoice == '3':
        print("You equip the ", weapon2[0])
        player[0] = weapon2
    elif weaponchoice == '4':
        print("You equip the ", weapon3[0])
        player[0] = weapon3
    elif weaponchoice == '5':
        if player[0][0] == 'barehands':
            print("You continue using nothing")
        else:
            print("You decide to keep your", player[0][0])
    else:
        print("You reach for a weapon but miss the handle, before you can react you are shoved through the gate into the pits unarmed")
        player[0] = WEAPONS[1]
def combat():
    global monster_int
    global alive
    monsterlife = ENEMIES[monster_int][4]
    playeraccuracy = player[0][3]
    monsteraccuracy = ENEMIES[monster_int][3]
    playermindamage = player[0][1]
    playermaxdamage = player[0][2]
    monstermindamage = ENEMIES[monster_int][1]
    monstermaxdamage = ENEMIES[monster_int][2]
    print("The", monster[0][0], " steps forward, prepared to fight, you must be too.")
    time.sleep(2)
    print("The", ENEMIES[monster_int][0], "charges at you, rolling to see who strikes first.")
    time.sleep(1)
    initiative = random.randint(1,20)
    print("You rolled", initiative)
    time.sleep(1)
    monsterinitiative = random.randint(1,20)
    print("The", ENEMIES[monster_int][0], "rolled", monsterinitiative)
    time.sleep(2)
    if initiative > monsterinitiative:
        print("You gain the iniative and attack first, choose 1-4")
        print("1. slash center mass")
        print("2. stab as accurately as possible")            
        print("3. smash with all your might")
        print("4. crash into the enemy")
        attackinput = int(input())
        if attackinput == 1:
              print("You attempt to slash the", ENEMIES[monster_int][0])
              time.sleep(1)
              accuracycheck = random.randint(0,10)
              if playeraccuracy >= accuracycheck:
                    playerhit = random.randint(playermindamage, playermaxdamage)
                    print("The blow lands! You deal", playerhit, "damage.")
                    time.sleep(2)
                    monsterlife = monsterlife - playerhit
                    if monsterlife >= 0:
                          print("The monster now has", monsterlife, "health.")
                          time.sleep(2)
              else:
                    print("The attack misses.")
                    time.sleep(2)
        elif attackinput == 2:                      
              print("You attempt to stab the", ENEMIES[monster_int][0])
              playeraccuracy2 = playeraccuracy + 1
              playermindamage2 = playermindamage - 1
              playermaxdamage2 = playermaxdamage - 1
              accuracycheck = random.randint(0,10)
              time.sleep(1)
              if playeraccuracy2 >= accuracycheck:
                    playerhit = random.randint(playermindamage2, playermaxdamage2)
                    print("The blow lands! You deal", playerhit, "damage.")
                    time.sleep(2)
                    monsterlife = monsterlife - playerhit
                    if monsterlife >= 0:
                          print("The monster now has", monsterlife, "health.")
                          time.sleep(2)
              else:
                    print("The attack misses.")
                    time.sleep(2)
        elif attackinput == 3:
              print("You attempt to smash the", ENEMIES[monster_int][0])
              playeraccuracy3 = playeraccuracy - 1
              playermindamage3 = playermindamage + 1
              playermaxdamage3 = playermaxdamage + 2
              accuracycheck = random.randint(0,10)
              time.sleep(1)
              if playeraccuracy3 >= accuracycheck:
                    playerhit = random.randint(playermindamage3, playermaxdamage3)
                    print("The blow lands! You deal", playerhit, "damage.")
                    time.sleep(2)
                    monsterlife = monsterlife - playerhit
                    if monsterlife >= 0:
                          print("The monster now has", monsterlife, "health.")
                          time.sleep(2)
              else:
                    print("The attack misses.")
                    time.sleep(2)
        elif attackinput == 4:
              print("You attempt to crash into the", ENEMIES[monster_int][0])
              playeraccuracy4 = playeraccuracy + 2
              playermindamage4 = playermindamage - 2
              playermaxdamage4 = playermaxdamage - 1
              accuracycheck = random.randint(0,10)
              time.sleep(1)
              if playeraccuracy4 >= accuracycheck:
                    playerhit = random.randint(playermindamage4, playermaxdamage4)
                    print("The blow lands! You deal", playerhit, "damage.")
                    time.sleep(2)
                    monsterlife = monsterlife - playerhit
                    if monsterlife >= 0:
                          print("The monster now has", monsterlife, "health.")
                          time.sleep(2)
              else:
                    print("The attack misses.")
                    time.sleep(2)
    while monsterlife > 0 and alive:
        accuracycheck2 = random.randint(0,10)
        if accuracycheck2 >= monsteraccuracy:
            monsterdamage = random.randint(monstermindamage, monstermaxdamage)
            print("The", ENEMIES[monster_int][0], "swipes at you for", monsterdamage)
            time.sleep(2)
            player[1] = player[1] - monsterdamage
            print("You now have", player[1], "health.")
            time.sleep(2)
        elif accuracycheck2 < monsteraccuracy:
            print("The", ENEMIES[monster_int][0], "misses you.")
            time.sleep(2)
        #monsters attack here
        if player[1] <= 0:
              alive = False
        elif player[1] > 0:
            print("Choose your attack: 1-4")
            time.sleep(.2)
            print("1. slash center mass")
            time.sleep(.2)
            print("2. stab as accurately as possible")
            time.sleep(.2)
            print("3. smash with all your might")
            time.sleep(.2)
            print("4. crash into the enemy")
            attackinput = int(input())
            if attackinput == 1:
                  print("You attempt to slash the", ENEMIES[monster_int][0])
                  time.sleep(1)
                  accuracycheck = random.randint(0,10)
                  if playeraccuracy >= accuracycheck:
                        playerhit = random.randint(playermindamage, playermaxdamage)
                        print("The blow lands! You deal", playerhit, "damage.")
                        time.sleep(2)
                        monsterlife = monsterlife - playerhit
                        if monsterlife >= 0:
                              print("The monster now has", monsterlife, "health.")
                              time.sleep(2)
                  else: 
                        print("The attack misses.")
                        time.sleep(2)
            elif attackinput == 2:                      
                  print("You attempt to stab the", ENEMIES[monster_int][0])
                  playeraccuracy2 = playeraccuracy + 1
                  playermindamage2 = playermindamage - 1
                  playermaxdamage2 = playermaxdamage - 1
                  accuracycheck = random.randint(0,10)
                  time.sleep(1)
                  if playeraccuracy2 >= accuracycheck:
                        playerhit = random.randint(playermindamage2, playermaxdamage2)
                        print("The blow lands! You deal", playerhit, "damage.")
                        time.sleep(2)
                        monsterlife = monsterlife - playerhit
                        if monsterlife >= 0:
                              print("The monster now has", monsterlife, "health.")
                              time.sleep(2)
                  else:
                        print("The attack misses.")
                        time.sleep(2)
            elif attackinput == 3:
                  print("You attempt to smash the", ENEMIES[monster_int][0])
                  playeraccuracy3 = playeraccuracy - 1
                  playermindamage3 = playermindamage + 1
                  playermaxdamage3 = playermaxdamage + 2
                  accuracycheck = random.randint(0,10)
                  time.sleep(1)
                  if playeraccuracy3 >= accuracycheck:
                        playerhit = random.randint(playermindamage3, playermaxdamage3)
                        print("The blow lands! You deal", playerhit, "damage.")
                        time.sleep(2)
                        monsterlife = monsterlife - playerhit
                        if monsterlife >= 0:
                              print("The monster now has", monsterlife, "health.")
                              time.sleep(2)
                  else:
                        print("The attack misses.")
                        time.sleep(2)
            elif attackinput == 4:
                  print("You attempt to crash into the", ENEMIES[monster_int][0])
                  playeraccuracy4 = playeraccuracy + 2
                  playermindamage4 = playermindamage - 2
                  playermaxdamage4 = playermaxdamage - 1
                  accuracycheck = random.randint(0,10)
                  time.sleep(1)
                  if playeraccuracy4 >= accuracycheck:
                        playerhit = random.randint(playermindamage4, playermaxdamage4)
                        print("The blow lands! You deal", playerhit, "damage.")
                        time.sleep(2)
                        monsterlife = monsterlife - playerhit
                        if monsterlife >= 0:
                              print("The monster now has", monsterlife, "health.")
                              time.sleep(2)
                  else:
                        print("The attack misses.")
                        time.sleep(2)
           else:
               print("You trip over a rock and scurry to your feet after a few seconds, but the monster is upon you already")
    if monsterlife <= 0:
                  print("You slay the", ENEMIES[monster_int][0], "and it topples to the ground.")
                  return True
    elif alive == False:
                return False

def bossfight():
    
    print("As you are about to enter the arena you are again presented with a choice of weapons:")
    time.sleep(3)
    weaponchoice()
    print("Upon entering the arena you smell blood in the air, the sun blinds you but as your eyes adjust you notice why...")
    time.sleep(5)
    print("The arena is slew with corpses and it is immediately apparent what created them.")
    time.sleep(4)
    print("Before you stands a",
def game():
    global alive
    bosscounter = bosscounter + random.randint(0,5)
    if bosscounter % random.randint(1,7) == 0:
        return bossfight()   
    monsterchoice()
    time.sleep(3)
    print("As you enter the arena your eyes fall upon a", monster[0][0])
    time.sleep(3)
    if bosscounter % 5 != 0:
        return combat()
    #return True or False



weaponchoice()
while alive == True:
    alive = game()
    if alive == True:
        #statboost()
        print("You wake up feeling reinvigorated and are prepared to fight another day")
        player[4] = player[4] + 1
        player[1] = player[2]
        time.sleep(4)
        amount = len(ENEMIES)
        newenemy = (ENEMIES[monster_int][0], ENEMIES[monster_int][1] + 1, ENEMIES[monster_int][2] + 1, ENEMIES[monster_int][3] + 1, ENEMIES[monster_int][4] + 1, ENEMIES[monster_int][5] + 20)
        ENEMIES.append(newenemy)
        player[5] = player[5] + ENEMIES[monster_int][5]
        print("You now have", player[5], "gold")
        time.sleep(2)
        print("You have won", player[4], "fights")
        time.sleep(2)
        #print("Would you like to visit the store")
        #MAYBE PUT A SHOP HERE
    elif alive == False:
        print("You died to the", ENEMIES[monster_int][0])
        print("you had", player[3], "gold")
        print("you killed", player[4], "enemies")
        quit
#print("died")
print(player)
print(monster)
