#!/usr/bin/env python3

import os
import time
import sys
import random

# ---------------- GLOBAL VARS -------------------
currentEnemy = 'Apostle'
attemptCounter = -1 # determines how many attempts the user has to pick the correct option

# --------------- DATA STRUCTURES -----------------
# Class `color` changes the properties of different pieces of text
# e.g. => print(color.BOLD + 'pancakes' + color.END) prints pancakes but in bold
class color:
    BOLD = '\033[1m'
    END = '\033[0m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'

def bold(x):
    x = color.BOLD + x + color.END
    print(x)

def red(x):
    x = color.RED + x + color.END
    print(x)

def blue(x):
    x = color.BLUE + x + color.END
    print(x)

def cyan(x):
    x = color.CYAN + x + color.END
    print(x)

# Dictionary that holds the stats of the player character
hero  = {
    "name": 'Hero',
    'lvl' : 1,
    'xp' : 0,
    'lvlNext' : 25, #how much xp is needed to level up
    'money' : 0,
    'stats' : {
        'str' : 1,
        'int' : 1,
        'hp'  : 50,
        'atk' : [5, 18],
        'luck' : 2,
        'mp' : 30
    }
}

# Dictionary that holds the stats of the enemy character
enemy = {
    "name" : "Apostle",
    "lvl" : "2",
    "xp" : '0',
    'reward': '25',
    'lvlNext' : 0,
    'stats' : {
    'str' : 1,
    'int' : 1,
    'hp'  : 50,
    'atk' : [5, 16],
    'luck' : 2,
    'mp' : 30
    }
}


# ---------------- UTILITY FUNCTIONS -------------------

# A quicktime event for typing in a specific word in a specific time, x is the word and y is the time
def typequick(x,y):
    print("Quickly! Type in the word",x)
    typequickans = input()
    y = time.time()

# utility function to clear the screen. This function is OS agnostic
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# basic function for dealing damage
# TODO: what does this function return?
def takeDmg(attacker, defender, enemy):
    dmg = random.randint(attacker['stats']['atk'][0],
                         attacker['stats']['atk'][1])
    defender['stats']['hp'] -= dmg

    if defender['stats']['hp'] <= 0:
        loser = blue('{} has been slain.'.format(defender['name']))
        if hero['name'] in loser:
            red('You have been slain...')
            print()
            print('Would to like to restart? (Y/N)')
            restartChoice = input()
            if restartChoice == 'Y':
                blue('Restarting...')
                time.sleep(3)
                clear_screen()
                time.sleep(2)
                combatSystem(hero, enemy)
                return hero['name']
            elif restartChoice == 'N':
                blue('Are you sure you want to quit? All progress will be lost.')
                quitChoice = input().capitalize()
                if quitChoice == 'Y' or 'Yes':
                    sys.exit()
        elif hero['name'] not in loser:
            blue(loser)
            hero['xp'] += enemy['reward']
            hero['money'] += enemy['reward']
            blue('You earned {} xp and {} runes!'.format(defender['reward']))
            time.sleep(3)
            bold('Clearing screen...')
            clear_screen()
            exit(0)
    else:
        blue('{} takes {} damage!'.format(defender['name'], dmg))

# Basic combatSystem
def combatSystem(player, enemy):
    global currentEnemy
    currentEnemy = enemy
    while True:
        print('-------------------------')
        cmd = input('Would you like to attack? (Y/N)').capitalize()
        if cmd == 'Y':
            print('You strike the enemy!')
            takeDmg(player, enemy, currentEnemy)
        elif cmd == 'N':
            print('While you\'re not paying attention, {} takes the opportunity to strike!'.format(enemy['name']))
            takeDmg(enemy, player, currentEnemy)

# ---------------- GAME LOGIC  -------------------
#The function for the opening title. useful for when the game restarts
def titleScreen():
    clear_screen()
    print("""
████████╗░██╗░░░░░░░██╗░█████╗░  ░██████╗██╗██████╗░███████╗░██████╗
╚══██╔══╝░██║░░██╗░░██║██╔══██╗  ██╔════╝██║██╔══██╗██╔════╝██╔════╝
░░░██║░░░░╚██╗████╗██╔╝██║░░██║  ╚█████╗░██║██║░░██║█████╗░░╚█████╗░
░░░██║░░░░░████╔═████║░██║░░██║  ░╚═══██╗██║██║░░██║██╔══╝░░░╚═══██╗
░░░██║░░░░░╚██╔╝░╚██╔╝░╚█████╔╝  ██████╔╝██║██████╔╝███████╗██████╔╝
░░░╚═╝░░░░░░╚═╝░░░╚═╝░░░╚════╝░  ╚═════╝░╚═╝╚═════╝░╚══════╝╚═════╝░""")
    print()
    print("There's two sides to every story...")
    print("Which is yours?")
    print(color.BOLD + "DISCLAIMER: IF THE PLAYER DOES NOT INPUT ONE OF THE GIVEN OPTIONS DUIRNG GAMEPLAY THEN THE GAME WILL RESTART." + color.END)
    print()
    print(color.BOLD + "Do you wish to play? (Y/N)" + color.END)
    startGame = input().capitalize()
    if startGame == "Y":
        intro()
    elif startGame == "N":
        print("That's too bad.")
    else:
        print("Please type Y or N.")
        time.sleep(3)
        titleScreen()

#a function that begins with the beginning of the story
def intro():
    global attemptCounter
    attemptCounter += 4
    print()
    print("The year is 2018 and you live in a modern world similar to the one individuals live in today. But there seems to be something off...")
    print("Doomsday seems to be approaching with every passing day, a nuclear war on the verge of execution.")
    print("A feeling of unease looms around the peripherals of every individual.")
    print("The world and it's people is in a state of involuntary collapse with corrupt politicians making poor decisions that have a global effect.")
    print("As judgement day begins to march forward, humanity begins to lose their morals and adopt new ones.")
    print()
    print("Anarchists known as the Dellos roam the city streets of rich neighborhoods, robbing, murdering and causing chaos")
    print("But a new unit of law enforcement has been implemented by the government to combat the anarchists and maintain order")
    print("Which side of conflict is most favorable for you?")
    print()
    print(color.BOLD + 'Option #1:' + color.END + " Anarchy and Chaos. The world is going to end anyway, who cares?")
    print(color.BOLD + 'Option #2:' + color.END + " Order and Peace. Why should you give up your morals due to actions from corrupt politicians?")
    print()
    #gives the user 3 attempts in picking the correct answer or the game will restart
    while attemptCounter >= 0:
        attemptCounter -= 1
        whichSide = input("Which side will you choose? (1/2): \n")
        if whichSide == '1':
            attemptCounter = -1
            print()
            path1()
        elif whichSide == '2':
            attemptCounter = -1
            print()
            path2()
        elif attemptCounter == 0:
            attemptCounter = -1
            print("You have 0 tries left")
            print("Thats a shame.")
            print("Going back to title screen...")
            time.sleep(3)
            titleScreen()
        else:
            print()
            print("Please type one of the given options.")
            print("You have",attemptCounter,"chance(s) left.")


# TODO: the function for path1 which branches out into different endings/scenarios
def path1():
    print("The choice has been made.")
    print()
    print("(EVERYTHING IS DARK)")

# TODO: the function for path2 which branches out into different ending / scenarios
def path2():
    global attemptCounter
    attemptCounter += 4
    print("The choice has been made.")
    print()
    print("(EVERYTHING IS LIGHT)")
    print("You take a glimpse at your surroundings realize you're in a dreamlike state.")
    print("The cascading clouds and glistening light shines through your transparent body as it guides you to an unknown path.")
    print("As you continue towards this path you see slight glimpses of a luminescent figure floating above you.")
    print("The initial sight of this causes you to feel skeptical, but you eventually adjust.")
    print("You continue following the lit trial until you hear an enchanthing voice.")
    print("The voice suprises you. And you stop for a second to analyze it.")
    print("Someone seems to be calling out to you.")
    print("There's something alluring about this voice, it almost seems familiar.")
    print()
    print(color.CYAN + '"Greetings. Traveler from beyond the light."' + color.END)
    print(color.CYAN + "...I am NELINA. I offer you an accord. ..." + color.END)
    print(color.CYAN + "...Have you heard of the LUMINESCENT LIGHT?..." + color.END)
    cyan('...It is the very source of energy in this field of light...')
    cyan('...The source of the light has properties that allows you to gain the abilites of mythological creatures...')
    cyan('...My kind live here to guide and assist travelers such as yourself...')
    cyan('...The light is kind of like a double-edged sword...')
    cyan('...Although the light supplies a seemingly endless amount of energy to these fields and grants extraordinary powers...')
    cyan('...Many travelers have lost their lives through their traversal...')
    cyan('...I can guide you, under one condition...')
    cyan('...You must reach the source of the light...')
    cyan('...The source of the light is rumored to reveal hidden secrets...')
    cyan('...I was born without parents, I wish to know my origins...')
    print()
    bold('What is your choice?')
    print(color.BOLD + 'Option #1:' + color.END, 'Take the offer from NELINA.')
    print(color.BOLD + 'Option #2:' + color.END, 'Decline the offer from NELINA.')

    while attemptCounter >= 0:
        attemptCounter -= 1
        path2Choice1 = int(input()) # you forgot to cast this to an `int` type. Remember that input() returns a `str` and you need an `int`
        if path2Choice1 == 1:
            attemptCounter = -1
            print()
            path2_1()
        elif path2Choice1 == 2:
            print()
            path2_2()
        elif attemptCounter == 0:
            print('Thats a shame.')
            print('Going back to title screen...')
            time.sleep(3)
            titleScreen()
        else:
            print()
            print("Please type one of the given options.")
            print("You have",attemptCounter,"chance(s) left.")

def path2_1():
    print()
    cyan('"Then it\'s settled."')
    cyan('...Summon me when you\'re lost for guidance towards the luminescent light...')
    print()
    print('NELINA\'s eyes slowing close as she dissolves into the light.')
    print('You follow the trial that NELINA left to guide you.')
    print('You see a ')
    print('All of a sudden the light shines more than 10x brighter.')
    print('')

def path2_2():
    print() 
    print("\n"+"The year is 2018 and you live in a modern world similar to the one individuals live in today. But there seems to be something off...")
    name = input("Please type the name you will be called throughout the game: ")
    print("Hello,",name+"!")
    while True:
        side = input("\nWhich side of the law do you want to be on? (Type With or Against): ").capitalize()
        if side == "With":
            clear_screen()
            break
        elif side == "Against":
            clear_screen()
            break
        else:
            print("Please type one of the given options")
    if side == "With":
        print("\n"+'\n'+'\n'+"You are a regular person in a regular suburban neighborhood. You constantly feel trapped in a cycle of consumerism with each passing day")
        print("You have a dream about a blue fairy like creature with an enchanting voice, chanting some sacred language that you never heard. There's something alluring about it's voice, it almost feels familiar..")
        print(color.CYAN + '???:' + color.END,"ИЖДВβψΣχΦΩπσγ, ИЖДВβψΣχΦΩπσγ¥§◎Штю€Ξ ВβψΣχΦΩπ ΦΩ innaR.\n")
        print("You're abrubtly woken up by a sharp noise. It appears to be your phone call, but it's from an unknown caller...")
        #choice 1 var
        print(color.BOLD + "What do you do?\n"+color.END + color.BOLD + '1:' + color.END,"Pick up the phone\n" + color.BOLD + '2:' + color.END,"Look around the house\n"+color.BOLD +'3:'+color.END,"Go back to sleep")
        while True:
            withchoice1 = int(input())
            if withchoice1 == 1:
                print("\nYou pick up the phone and hear a mysterious voice ushering random numbers and equations")
                print(color.RED + 'unknown:' + color.END + "49.131883. 9.160123. 49 7' 54.7788. 9 9' 36.4428")
                break
            elif withchoice1 == 2:
                print("You look around your house and find that you're mom who is usually in the living room watching TV is gone. Yet the TV is on her favorite channel...something is off...")
                break
            elif withchoice1 == 3:
                print("You tell the caller to fuck off, thinking it's a scam. As you lie back in bed trying to remember that dream, you get a call back from your employer that you previously had an interview with.")
                break
            else:
                print("Please type 1, 2 or 3")
            #next steps if player chooses to pick up the phone
                if withchoice1 == 1:
                    while True:
                        print(color.BOLD + 'What is your next move?\n' + color.END + color.BOLD + '1:' + color.END + 'Say something\n' + color.BOLD + '2:' + color.END + 'Search up the numbers' + color.BOLD + '3:' + color.END + 'Hang up')
                    #the third choice leads to the bad ending
                        withchoice2 = int(input())
                        if withchoice2 == 1:
                            input("What do you wish to say?\n")
                            print(color.RED + 'unknown:' + color.END,"*laughs maniacally* You really have no idea do you?......think geographically.")
                        elif withchoice2 == 2:
                            print("You search up the numbers on google and it shows a google maps link to an abandon warehouse that you and your friends would explore as kids")
                        elif withchoice2 == 3:
                            print("You hang up the phone but the phone continues to rings again from that same unknown caller.")
                            break
                        else:
                            print("Please type 1, 2 or 3")
                if withchoice2 == 3:
                    #this series of choices leads to the bad ending
                    while True:
                        print(color.BOLD + "What do you do now?\n" + color.END + color.BOLD + '1:' + color.END, 'Destroy your phone.')
                        badendingchoice1 = int(input())
                        if badendingchoice1 == 1:
                            print("\n You grab the metal bat from under your bed.")
                            print("As you're holding the bat in your hand, ready to destroy the problem, you get a text message from the unknown caller.")
                            print(color.RED + 'unknown: dont do it.' + color.END)
                            print("You do it anyway and batter your helpless phone screen as it shatters into pieces.")
                            for x in range(1,10):
                                print(color.BLUE + 'Cellphone' + color.END, 'BEEP')
                        else:
                            print("Pick your choice : )")


# ---------------- MAIN GAME LOOP  -------------------

if __name__ == "__main__":
    intro()
