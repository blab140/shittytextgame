import time
import random


#when creating new bosses need to edit bossability, bossdialogue, weakpoint and bossappend
def print_pause(lines):
    for (line, pause) in lines:
            print(line)
            time.sleep(pause)
            
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print("WELCOME TO THE FIGHT PITS")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")

time.sleep(3)

bosschoice = BOSSES[0]
monster_int = 0
alive = True
bosscount = 0
bossabilityflip = 0
bossabilitycount = 0

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
BOSSES = [('Wyvern', 2, 4, 7, 30, 1000, 1, 1),]
#name, attack min, attack max, accuracy, health, gold dropped, boss factor(stat increases on the new boss append), player accuracy subtracter
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
        player[3] = player[3] + goldreward_int
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
    print("The", ENEMIES[monster_int][0], "charges at you: rolling to see who strikes first.")
    time.sleep(1)
    initiative = random.randint(1,20)
    print("You rolled", initiative)
    time.sleep(1)
    monsterinitiative = random.randint(1,20)
    print("The", ENEMIES[monster_int][0], "rolled", monsterinitiative)
    time.sleep(2)
    if initiative > monsterinitiative:
      if player[0] == WEAPONS[1] or player[0] == WEAPONS[0]:
        print("You gain the iniative and attack first, choose 1-4")
        print("1. chop center mass")
        print("2. jab as accurately as possible")            
        print("3. smash with all your might")
        print("4. crash into the enemy")
        attackinput = int(input())
        if attackinput == 1:
              print("You attempt to chop the", ENEMIES[monster_int][0])
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
              print("You attempt to jab the", ENEMIES[monster_int][0])
              playeraccuracy2 = playeraccuracy + 1
              playermindamage2 = playermindamage - 1
              if playermindamage2 < 0:
                      playermindamage2 = 0
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
              if playermindamage4 < 0:
                      playermindamage4 = 0
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
                    #ABOVE THIS IS BAREHANDS
      else:      
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
              if playermindamage2 < 0:
                      playermindamage2 = 0
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
              if playermindamage4 < 0:
                      playermindamage4 = 0
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
            if player[0] == WEAPONS[1] or player[0] == WEAPONS[0]:
                        print("You gain the iniative and attack first, choose 1-4")
                        print("1. chop center mass")
                        print("2. jab as accurately as possible")            
                        print("3. smash with all your might")
                        print("4. crash into the enemy")
                        attackinput = int(input())
                        if attackinput == 1:
                              print("You attempt to chop the", ENEMIES[monster_int][0])
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
                              print("You attempt to jab the", ENEMIES[monster_int][0])
                              playeraccuracy2 = playeraccuracy + 1
                              playermindamage2 = playermindamage - 1
                              if playermindamage2 < 0:
                                      playermindamage2 = 0
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
                              if playermindamage4 < 0:
                                      playermindamage4 = 0
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
            else:
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
                      if playermindamage2 < 0:
                          playermindamage2 = 0
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
                      if playermindamage4 < 0:
                          playermindamage4 = 0
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
def bossdialogue():
    if bosschoice[0] == 'Wyvern':
        print("The Wyvern is a fierce foe and will take everything you have to overcome it")
        time.sleep(3)
        print("Be careful of it's ability to breathe fire and fly in the arena")
def bossappend():
    if bosschoice[0] == 'Wyvern':
def bossability():
    global bossabilityflip
    global bossabilitycount
    global bosschoice
    if bosschoice[0] == 'Wyvern':    
        bossabilityflip = random.randint(0, 1)
        if bossabilityflip == 0:
            print("The Wyvern inhales sharply it is sure to breathe fire next turn.")
            time.sleep(4)
            print("Please choose 1-4")
            #player has choice to hide from next turns fire (rng) or keep fighting for critical strike
        if bossabilityflip ==1:
            print("The Wyvern jumps into the air and flaps it's wings. It takes off.")
            #wyvern attacks multiple times uninterupted
def bosschoice():
    global bosschoice
    global BOSSES
    global bosscount
    bosschoice = random.choice(BOSSES)
def weakpoint():
    if bosschoice[0] == 'Wyvern':
        return('neck')
def bossfight():
    return True
    global bosschoice
    global alive
    bosshealth = bosschoice[4]
    bosschoice()
#comment this out lazy fuck
    print("As you are about to enter the arena you are again presented with a choice of weapons:")
    time.sleep(3)
    weaponchoice()
    print("Upon entering the arena you smell blood in the air, the sun blinds you but as your eyes adjust you notice why...")
    time.sleep(5)
    print("The arena is slew with corpses and it is immediately apparent what created them.")
    time.sleep(4)
    print("Before you stands a", bosschoice[0])
    time.sleep(2)
    if bosscount == 0
        print("During this fight you will have to fight a boss and deal with it's special attacks.")
        time.sleep(3)
    bosscount = bosscount + 1
    bossname = bosschoice[0]
    bossdialogue()
    weakpoint = weakpoint()
    bosses = bosschoice[0] + "'s"
    print("Rolling for initiative")
    time.sleep(2)
    playerinitiative = random.randint(1, 20)
    bossinitiative = random.randint(1, 20)
    print("You roll", playerinitiative, "against the bosses", bossinitiative)
    time.sleep(3)
    if playerinitiative > bossinitiative:
        print("Please choose 1-4")
        time.sleep(1)
        if player[0] == WEAPONS[1] or player[0] == WEAPONS[0]:
            print("1. Punch the", bosschoice[0])
        else:
            print("1. Slash at the", bosschoice[0])
        if player[0] == WEAPONS[1] or player[0] == WEAPONS[0]:
            print("2. Smash the", bosschoice[0], "with your fists"
        else:
            print("2. Smash the", bosschoice[0], "with your", player[0][0])
        if player[0] == WEAPONS[1] or player[0] == WEAPONS[0]:
            print("3. Try to kick the", bosses, weakpoint)
        else:
            print("3. Aim for the", bosses, weakpoint)
        if player[0] == WEAPONS[1] or player[0] == WEAPONS[0]:
            print("4. Go all highlander on the", bosschoice[0])
        else:
            print("4. Attempt to charge the", bosschoice[0])
        attackinput = int(input())
        if attackinput == 1:
            if player[0] == WEAPONS[1] or player[0] == WEAPONS[0]:
                 print("You attempt to punch the", bosschoice[0])
                  time.sleep(2)
            else:
                print("You attempt to slash the", bosschoice[0])
                  time.sleep(2)
            accuracycheck = random.randint(0, 10)
            if player[0][3] - bosschoice[7] > accuracycheck:
                  damage = random.randint(player[0][1], player[0][2])
                  bosshealth = bosshealth - damage
                  print("The strike hits!")
                  time.sleep(1)
                  print("You deal", damage, "damage")
                  print("The", bosschoice[0], "now has", bosshealth, "health")
            else:
                  print("You missed!")
                  time.sleep(1)
    else:
        while bosslife > 0 and alive:
                  bossability = random.randint(0, 5)
                  if bossability == random.randint(0, 5):
                      bossability()
                  else:
                      #boss attacks

                  
                  
bosscounter = 1          
def game():
    global alive
    global bosscounter
    bosscounter = bosscounter + random.randint(0,5)
    bosscounter2 = random.randint(1,7)
    if bosscounter % bosscounter2 == 0:
        return bossfight()   
    if bosscounter % bosscounter2 != 0:
        monsterchoice()
        time.sleep(3)
        print("As you enter the arena your eyes fall upon a", monster[0][0])
        time.sleep(3)
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
        player[3] = player[3] + ENEMIES[monster_int][5]
        print("You now have", player[3], "gold")
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
