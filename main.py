# Michael Bryan
# COP 1500
# Professor Vanselow
# Integration Project
#
# This project is a dungeon crawler in the modern day world! You'll
# be fighting
# your way through the workplace trying to get a raise from your
# boss.

# Setup random number generator
import random


def correct_Input(userInput, choice1, choice2=None, choice3=None,
                  choice4=None):
    if (userInput == choice1):
        return True
    elif (userInput == choice2):
        return True
    elif (userInput == choice3):
        return True
    elif (userInput == choice4):
        return True
    else:
        return False


def running_module(running, distance, randomVar, defense, luck, health,
                   isEffective):
    if (running == 0):
        print("You run out of your cubicle...\n")
        randomVar = int(random.random() * 10)
        if (defense - randomVar < 0):
            print("and you definitely just tripped and fell "
                  "straight on your face")
            isEffective = False
            return isEffective
    if (running == 1):
        print("you run pass one office")
    if (running == 2):
        randomVar = int(random.random() * 10)
        if (luck - randomVar < 0):
            print("Boss sees you running! You immediately "
                  "stop and are forced to talk to him.")__author__ = "Michael Bryan"

# COP 1500
# Professor Vanselow
# Integration Project
#
""""This project is a dungeon crawler in the modern day world!
You'll be fighting your way through the workplace trying to get
a raise from your boss. Part 1 of 5. In order to play more, download
the additional DLC from your School bookstore."""

# Setup random number generator
import random


def correct_input(user_input, choice1, choice2=None,
                  choice3=None, choice4=None):
    """Checks to see if the user's input is correct or not. Write about
    parameters for all function parameters."""
    if user_input == choice1:
        return True
    elif user_input == choice2:
        return True
    elif user_input == choice3:
        return True
    elif user_input == choice4:
        return True
    else:
        return False


def running_module(distance, random_var, defense, luck,
                   health):
    """This is the running module that is used within main."""
    is_effective = None
    if distance == 0:
        print("You run out of your cubicle...\n")
        if defense - random_var < 0:
            print("and you definitely just tripped and fell "
                  "straight on your face")
            is_effective = False
            return is_effective
    if distance == 1:
        print("you run pass one office")
    if distance == 2:
        random_var = int(random.random() * 10)
        if luck - random_var < 0:
            print("Boss sees you running! You immediately "
                  "stop and are forced to talk to him.")
            is_effective = False
            return is_effective
        else:
            print("Oh phew... your boss was turned the other"
                  " way and didn't see you.")
            print("+5 Evasiveness (Not an actual attribute.)")
            is_effective = True
            return is_effective
    if distance == 3:
        if random_var <= .3:
            print("Ooooh, you're getting out of breath. Too many "
                  "donuts from the break room.")
            is_effective = False
            return is_effective
        elif .3 < random_var < .7:
            print("You're panting, but you keep going.")
            return is_effective
        elif random_var >= .7:
            print("")
    if distance == 4:
        if random_var <= .5:
            print("Whoa, look at you go, buddy! You're fast! You wind"
                  " up in front of a vending machine w/ snacks. You"
                  " pull out a dollar and get a Big Kat Kit Kat "
                  "(sponsored) in exchange.")
            is_effective = True
            return is_effective
        else:
            print("You ran into someone and spilled someone's "
                  "coffee. Yikes.")
            is_effective = False
            return is_effective
    if distance == 5:
        random_var = int(random.random() * 10)
        if random_var > luck + (health / 10) // 2:
            input("Looks like you weren't lucky or fit enough, you "
                  "pulled a hamstring.")
            is_effective = False
            return is_effective
        elif random_var == luck + (health / 10) // 2:
            print("Lil' out of breath, but you'll be fine.")
            is_effective = True
            return is_effective
        else:
            print("Lil' office jog ain't bad")
            is_effective = True
            return is_effective


def end_show_stats(health, caffeine, luck, attack, defense, choice,
                   act1eff):
    """Shows end of game stats"""
    print("\n------------------------------")
    print("END OF ACT 1\n\nStats-")
    print("Health: ", format(health, '0.2f'))
    print("Caffeine: ", format(caffeine, '0.2f'))
    print("Luck: ", format(luck, '0.2f'))
    print("Attack: ", format(attack, '0.2f'))
    print("Defense: ", format(defense, '0.2f'))
    if choice == 'Y':
        print("Act 1 Choice: Yell to Evan")
    elif choice == 'I':
        print("Act 1 Choice: Ignore Evan")
    elif choice == 'R':
        print("Act 1 Choice: Run Pass Evan")
    elif choice == 'W':
        print("Act 1 Choice: Walk to Evan")
    print("Act 1 Effectiveness: ", act1eff)
    print("------------------------------\n")


def main():
    """This is the main program (Part 1/5) of the dungeon crawler."""
    # Create local variables for use in dungeon crawling
    action1_effective = None
    random_var = 0.0

    # Introduce the user to the game.
    print("Welcome traveler! You will be embarking throughout "
          "the office to get a raise")
    print("from your boss. Will you make it through the "
          "gauntlet? Will you meet your")
    print("destiny or will you suffer a terrible fate? Only you "
          "can decide your path.\n")

    # Tells user how to play the game.
    print("Rules to play: \nSelect answers that are within (_) of a "
          "word. Example - (A)ttack.")
    print("Enter 'A' to attack.")
    print("Press Enter when prompted to roll.\n" * 1)

    # Get the User's character name
    first_name = input("Input your character's first name: ")
    last_name = input("Input your character's last name: ")
    full_name = first_name + " " + last_name

    # Checks to make sure name isn't a number
    good_name = False
    while not good_name:
        if first_name.isnumeric() or last_name.isnumeric():
            print("Accounting won't let you have numbers as your"
                  " name. Try again.")
            if first_name.isnumeric() and \
                    last_name.isnumeric():
                first_name = input("First name: ")
                last_name = input("Last name: ")
            elif first_name.isnumeric():
                first_name = input("First name: ")
            elif last_name.isnumeric():
                last_name = input("Last name: ")
            full_name = first_name + " " + last_name
            good_name = False
        else:
            print("\n", full_name, ", your name will live on forever... "
                                   "or as long as this company lasts.",
                  sep='')
            good_name = True

    # Pleasantries for the programmer
    if full_name == "Michael Bryan":
        print("\nWelcome back, Master.")
    if full_name != "Michael Bryan":
        print("\nYou are about to embark on a journey.")

    # Rolling for stats
    print("\nNow you must roll for your stats.")
    input("Press Enter for your Health Stat. (1-100)")
    health = (random.random() * 100) % 100
    print("Health: ", format(health, '3.0f'), sep='')
    input("Press Enter for your Caffeine Stat. (0-10)")
    caffeine = (random.random() * 100) // 10
    print("Caffeine: ", format(caffeine, '1.0f'))
    input("Press Enter for your Luck Stat. (0-10)")
    luck = (random.random() / .01) % 10
    print("Luck: ", format(luck, '2.0f'))
    input("Press Enter for your Attack Stat. (0-10)")
    attack = (random.random() * 100) // 10
    print("Attack: ", format(attack, '1.0f'))
    input("Press Enter for your Defense Stat. (0-10)")
    defense = (random.random() * 100) // 10
    print("Defense: ", format(defense, '1.0f'))
    print("End of Stats.")

    # Begin Dungeon
    print("\nYou awaken at your desk after a short nap. Very lucky "
          "that your boss didn't")
    print("see you. You get up and look over your cubicle to see a "
          "coworker, named Evan.")
    print("You decide to (Y)ell at Evan, (I)gnore him and get coffee, "
          "(R)un pass him, or (W)alk up to him.\n")
    action1 = str(input("Your response: "))

    # Checks to see if input is correct
    while not correct_input(action1, 'Y', 'I', 'R', 'W'):
        action1 = str(input("Try Again: "))

    # Branch of first action
    while (action1 == 'Y' or action1 == 'I' or action1 == 'R' or action1
           == 'W'):
        if action1 == 'Y':  # Yell Action
            input("You decide to Yell. Roll (by pressing Enter) to see "
                  "if effective.")

            # Rolls for Yelling to Evan
            if (random.random() * 100) // 10 - attack <= 1:
                is_effective = True
            else:
                is_effective = False

            # Action taken after roll
            if is_effective:
                action1_effective = True
                print("You got Evan's attention, he's walking over.")
                break
            elif not is_effective:
                action1_effective = False
                print("Evan did not hear you.")
                break
        elif action1 == 'I':  # Ignore Action
            input("You go to the coffee machine and pour a cup. "
                  "Roll for effectiveness.")
            random_var = int(random.random() * 10)
            if 0 <= random_var < 3:
                print("This coffee is pretty weak. Almost no caffeine"
                      " boost.")
                action1_effective = False
                if caffeine + (random_var / 10) ** random_var > 10:
                    caffeine = 10
                    break
                else:
                    caffeine = (random_var / 10) ** random_var
                    break
            elif 3 <= random_var < 8:
                print("This coffee is moderately strong. Sweet spot.")
                action1_effective = True
                if caffeine + random_var > 10:
                    caffeine = 10
                    break
                else:
                    caffeine += random_var
                    break
            elif 8 <= random_var < 10:
                print("You drank Cuban coffee! You're too jittery! "
                      "Health affected.")
                action1_effective = False
                caffeine = 10
                health /= 10
                break
            elif random_var == 10:
                print("You somehow broke the game. Coffee is every"
                      "where. No boost.")
                action1_effective = False
                break
        elif action1 == 'R':  # Run Action
            print("You will now be running (see what I did there?) a "
                  "series of tests. ")
            distance = int(input("How many meters"
                                 "pass him (1-5)? "))
            while distance < 1 or distance > 5:
                try:
                    distance = int(input("Distance: "))
                    print("Valid Input.")
                    break
                except ValueError:
                    print("Invalid input. Please try again. 1-5")
            action1_effective = running_module(distance, random_var,
                                               defense, luck, health)
            break
        elif action1 == 'W':
            random_var = random.random()
            if random_var <= .3:
                print("Abruptly, you're stopped by your boss. He wants"
                      "to ask you about the memo that was sent out.")
                print("You shuffle around but ultimately give a lame "
                      "excuse that you haven't read it yet.")
                action1_effective = False
            if .3 < random_var < .7:
                print("You casually walk over to Evan. He asks if you"
                      "read the memo that the boss sent this morning."
                      " Apparently, there's a list of people that will be "
                      "fired. Office Gossip is amok.")
                action1_effective = True
            if random_var >= .7:
                print("Evan tells you about the memo about people"
                      " getting fired. He checked for you and you're not"
                      " on it.")
                action1_effective = True
            break
        else:
            print("Game has broken somehow. Exiting")
            action1_effective = False
            break
    end_show_stats(health, caffeine, luck, attack, defense, action1,
                   action1_effective)


main()

            isEffective = False
            return isEffective
        else:
            print("Oh phew... your boss was turned the other"
                  " way and didn't see you.")
            print("+5 Evasiveness (Not an actual attribute.)")
            isEffective = True
            if (running == distance):
                return isEffective
    if (running == 3 and distance == 3):
        print("Ooooh, you're getting out of breath. Too many "
              "donuts from the break room.")
        isEffective = True
        return isEffective
    else:
        print("You're panting, but you keep going.")
    if (running == 4):
        print("Whoa, look at you go, buddy! You're fast!")
        isEffective = True
        if (running == distance):
            return isEffective
    if (running == 5):
        randomVar = int(random.random() * 10)
        if (randomVar > luck + (health / 10) // 2):
            input("Looks like you weren't lucky or fit enough, you pulled a "
                  "hamstring.")
            isEffective = False
            return isEffective
        elif (randomVar == luck + (health / 10) // 2):
            print("Lil' out of breath, but you'll be fine.")
            isEffective = True
            return isEffective
        else:
            print("Lil' office jog ain't bad")
            isEffective = True


def main():
    # Create local variables for use in dungeon crawling
    goodName = None
    action1 = None
    action1Effective = None
    action2 = None
    action2Effective = None
    action3 = None
    action3Effective = None
    action4 = None
    action4Effective = None
    randomVar = None
    isEffective = None
    repeat_RunModule = None
    TCQVar = None

    # Introduce the user to the game.
    print("Welcome traveler! You will be embarking throughout "
          "the office to get a raise")
    print("from your boss. Will you make it through the "
          "gauntlet? Will you meet your")
    print("destiny or will you suffer a terrible fate? Only you "
          "can decide your path.\n")

    # Tells user how to play the game.
    print("Rules to play: \nSelect answers that are within (_) of a "
          "word. Example - (A)ttack.")
    print("Enter 'A' to attack.")
    print("Press Enter when prompted to roll.\n" * 1)

    # Get the User's character name
    firstName = input("Input your character's first name: ")
    lastName = input("Input your character's last name: ")
    fullName = firstName + " " + lastName

    # Checks to make sure name isn't a number
    goodName = False
    while (goodName == False):
        if (firstName.isnumeric() == True or lastName.isnumeric()
                == True):
            print("Accounting won't let you have numbers as your"
                  " name. Try again.")
            if (firstName.isnumeric() == True and lastName.isnumeric()
                    == True):
                firstName = input("First name: ")
                lastName = input("Last name: ")
            elif (firstName.isnumeric() == True):
                firstName = input("First name: ")
            elif (lastName.isnumeric() == True):
                lastName = input("Last name: ")
            fullName = firstName + " " + lastName
            goodName = False
        else:
            print("\n", fullName, ", your name will live on forever... or "
                                  "as long as this company lasts.", sep='')
            goodName = True

    # Pleasantries for the programmer
    if (fullName == "Michael Bryan"):
        print("\nWelcome back, Master.")
    if (fullName != "Michael Bryan"):
        print("\nYou are about to embark on a journey.")

    # Rolling for stats
    print("\nNow you must roll for your stats.")
    input("Press Enter for your Health Stat. (1-100)")
    health = (random.random() * 100) % 100
    print("Health: ", format(health, '3.0f'), sep='')
    input("Press Enter for your Caffeine Stat. (0-10)")
    caffeine = (random.random() * 100) // 10
    print("Caffeine: ", format(caffeine, '1.0f'))
    input("Press Enter for your Luck Stat. (0-10)")
    luck = (random.random() / .01) % 10
    print("Luck: ", format(luck, '2.0f'))
    input("Press Enter for your Attack Stat. (0-10)")
    attack = (random.random() * 100) // 10
    print("Attack: ", format(attack, '1.0f'))
    input("Press Enter for your Defense Stat. (0-10)")
    defense = (random.random() * 100) // 10
    print("Defense: ", format(defense, '1.0f'))
    print("End of Stats.")

    # Begin Dungeon
    print("\nYou awaken at your desk after a short nap. Very lucky "
          "that your boss didn't")
    print("see you. You get up and look over your cubicle to see a "
          "coworker, named Evan.")
    print("You decide to (Y)ell at Evan, (I)gnore him and get coffee, "
          "(R)un pass him,")
    print("or (W)alk up to him.\n")
    action1 = str(input("Your response: "))

    # Checks to see if input is correct
    while (not correct_Input(action1, 'Y', 'I', 'R', 'W')):
        action1 = str(input("Try Again: "))

    # Branch of first action
    while (action1 == 'Y' or action1 == 'I' or action1 == 'R' or action1
           == 'W'):
        if (action1 == 'Y'):  # Yell Action
            input("You decide to Yell. Roll (by pressing Enter) to see "
                  "if effective.")

            # Rolls for Yelling to Evan
            if ((random.random() * 100) // 10 - attack <= 1):
                isEffective = True
            else:
                isEffective = False

            # Action taken after roll
            if (isEffective == True):
                action1Effective = True
                print("You got Evan's attention, he's walking over.")
                break
            elif (isEffective == False):
                action1Effective = False
                print("Evan did not hear you.")
                break
        elif (action1 == 'I'):  # Ignore Action
            input("You go to the coffee machine and pour a cup. "
                  "Roll for effectiveness.")
            randomVar = int(random.random() * 10)
            if (randomVar >= 0 and randomVar < 3):
                print("This coffee is pretty weak. Almost no caffeine"
                      " boost.")
                action1Effective = False
                if (caffeine + (randomVar / 10) ** randomVar > 10):
                    caffeine = 10
                else:
                    caffeine = (randomVar / 10) ** randomVar
            elif (randomVar >= 3 and randomVar < 8):
                print("This coffee is moderately strong. Sweet spot.")
                action1Effective = True
                if (caffeine + randomVar > 10):
                    caffeine = 10
                else:
                    caffeine += randomVar
            elif (randomVar >= 8 and randomVar < 10):
                print("You drank Cuban coffee! You're too jittery! "
                      "Health affected.")
                action1Effective = False
                caffeine = 10
                health /= 10
            elif (randomVar == 10):
                print("You somehow broke the game. Coffee is every"
                      "where. No boost.")
                action1Effective = False
                break
        elif (action1 == 'R'):  # Run Action
            print("You will now be running (see what I did there?) a "
                  "series of tests. ")
            distance = int(input("How many meters pass him (1-5)? "))
            while (distance < 1 or distance > 5):
                if (distance < 1):
                    distance = int(input("Too short of a distance."))
                else:
                    distance = int(input("Too far of a distance."))
            repeat_RunModule = int(input("Number of attempts to "
                                         "win? (1-5)"))
            while (repeat_RunModule < 1 or repeat_RunModule > 5):
                repeat_RunModule = int(input("Try again (1-5)"))
            for repeat_RunModule in range(distance):
                run_Outcome = running_module(repeat_RunModule, distance,
                                             randomVar,
                                             defense, luck, health,
                                             isEffective)
                isEffective = run_Outcome
                if (run_Outcome == True):
                    break
                else:
                    TCQVar = input("You failed multiple times, (T)ry "
                                   "again, (C)ontinue, or (Q)uit?")
                    while (TCQVar != 'T' and TCQVar != 'C' and TCQVar
                           != 'Q'):
                        TCQVar = input("Answer: ")
                    if (TCQVar == 'T'):
                        repeat_RunModule = int(input("How many attempts"
                                                 " to win"))
                        while (repeat_RunModule < 1 or repeat_RunModule > 5):
                            repeat_RunModule = int(input("Try again (1-5)"))
                        for repeat_RunModule in range(distance + 1):
                            if (running_module(repeat_RunModule, distance,
                                               randomVar, defense, luck,
                                               health,
                                               isEffective) == True):
                                break
                    if (TCQVar == 'C'):
                        input("You've chosen the following for your first "
                              "Action (Press Enter)")
                        print("Health: ", format(health, '3.0f'), sep='')
                        print("Caffeine: ", format(caffeine, '3.0f'), sep='')
                        print("Luck: ", format(luck, '3.0f'), sep='')
                        print("Attack: ", format(attack, '3.0f'), sep='')
                        print("Defense: ", format(defense, '3.0f'), sep='')
                        print("Effectiveness: ", isEffective, sep='')
                        break
                    if (TCQVar == 'Q' or TCQVar == 'C'):
                        break
                if (TCQVar == 'Q' or TCQVar == 'C'):
                    break
            if (TCQVar == 'Q' or TCQVar == 'C'):
                break
            break
        #elif (action1 == 'W'):
         #   break
        else:
            break


main()
