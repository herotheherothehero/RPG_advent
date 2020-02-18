import random
import time
def main():
    hp_stat = random.sample([0,1,2,3,4,5,6,7,8,9],1)
    strength_stat = random.sample([0,1,2,3,4,5,6,7,8,9],1)
    speed_stat = random.sample([0,1,2,3,4,5,6,7,8,9],1)
    magic_stat = random.sample([0,1,2,3,4,5,6,7,8,9],1)
    luck_stat = random.sample([0,1,2,3,4,5,6,7,8,9],1)
    print(hp_stat, strength_stat, speed_stat, magic_stat, luck_stat)
    name = input('Hello, What is your name traveler? ')
    time.sleep(.5)
    print("...")
    time.sleep(.5)
    print(f"{name} huh? Is it really you?")
    name_confirm = input("yes or no ")
    if name_confirm == "yes":
        print(f"\nWell then {name},  if it really is you then are you a boy or a girl? ")
        gender = input("Boy or Girl (Please choose one and im sorry if im not being progressive but if you decide you're neither the code isnt gonna work... ")
        if gender == "boy":
            print(f"Then it must really be you! {name} the Magnificent!")
            print('Slayer of many and "layer" of even more ;)')
            print("\nDo you wish to embark on a journey based primarily\non how lucky you were at the time of creation?")
            advent_confirm = input("Yes or No ")
            if advent_confirm == "Yes" or "yes" or "y" or "Y":
                print("\nThen lets get started, lets see what you start with: ")
                print(f"\nHp:{hp_stat}\nStrength:{strength_stat}\nSpeed:{speed_stat}\nMagic:{magic_stat}\nLuck:{luck_stat}")
                print("...")
                time.sleep(1)
                print("Well, you got what you got, time to begin!")
        elif gender == "girl":
            print(f"\nThen it must really be you! {name} the Goddess~!")
            print('Slayer of many and "conqueror" of even more!')
            print("\nDo you wish to embark on a journey based primarily\non how lucky you were at the time of creation?")
            advent_confirm = input("Yes or No ")
        if advent_confirm =="yes":
            print("\nThen lets get started, lets see what you start with: ")
            print(f"\nHp:{hp_stat}\nStrength:{strength_stat}\nSpeed:{speed_stat}\nMagic:{magic_stat}\nLuck:{luck_stat}")
            print("...")
            time.sleep(1)
            print("Well, you got what you got, time to begin!")
    else: 
        print("Start over")
        time.sleep(1.5)
    move_number = 0
    print("You wake up in the forest with nothing but")
    print("raggedy clothes and the faint memory of")
    print("agreeing to this")
    if q1 =="yes":
        print("For testing my game, enjoy the bonus!")
        guide_bonus = random.sample([0,1,2,3,4],1)
        if guide_bonus[0] == 0:
            print("Health buff!")
            hp_stat[0]+= 1
        elif guide_bonus[0] == 1:
            print("Strength buff!")
            strength_stat[0]+= 1
        elif guide_bonus[0] == 2:
            print("Speed buff!")
            speed_stat[0]+= 1
        elif guide_bonus[0] == 3:
            print("Magic buff!")
            magic_stat[0]+= 1
        elif guide_bonus[0] == 4:
            ("Luck buff!")
            luck_stat[0]+= 1

        elif q1 =="no":
            print("Nothing happened, The gods are displeased nonetheless")
    for move_number in range(20):    
        move1 = input("What will you do?")
        if move1 == 'help':
            if hp_stat[0] and strength_stat[0] and speed_stat[0] and magic_stat[0] and luck_stat[0] < 5:
                print("You are a peasant, ngl you can't really do anything (Challenge mode)")
            elif strength_stat[0] >= 9 and speed_stat[0] <= 5 and hp_stat[0] <= 5 and magic_stat[0] <= 5 and luck_stat[0] <= 5:
                print("You are a tough guy who is good at nothing else, you are able to 'intimidate' enemies and 'break' more")
            elif speed_stat[0] >= 9 and strength_stat[0] <= 9 and hp_stat[0] <= 5 and magic_stat[0] <= 5 and luck_stat[0] <= 5:
                print(f"You should be considered the fastest man alive,\nwatch as you are able to 'flee' from any battle you wish in the blink of an eye!\ngoing supersonic isnt a problem for you, {name}")
            elif hp_stat[0] >= 9 and strength_stat[0] <= 9 and speed_stat[0] <= 5 and magic_stat[0] <= 5 and luck_stat[0] <= 5:
                print("You have the biggest of hearts, and for that you are able to 'spare'\nanyone you deem worthy, if they dont agree, you can always 'regen' in battle!")
            elif magic_stat[0] >= 9 and strength_stat[0] <= 9 and speed_stat[0] <= 5 and hp_stat[0] <= 5 and luck_stat[0] <= 5:
                print(f"Oh lookie here it's your typical sorceror {name}!,\nit looks as if you are able to use 'spell' to conjure up any number of things!\nFrom a fire spell to an instant death spell! How Cool!")
            elif luck_stat[0] >=9 and strength_stat[0] <= 9 and speed_stat[0] <= 5 and magic_stat[0] <= 5 and hp_stat[0] <= 5:
                print(f"The luckiest lad in all the land {name}! Today, RN-Jesus is on your side!\n You could always try to 'wish' for something and with your insane luck, you may just get it!(Given that its in the game)")
            elif
                
                
                
                
                
                
                
                
                
                
                
                
                
                move_number += 1
                continue
        elif move1 == "look around":
            print("You take a look at your surroundings and\nnotice a 'note' beside you. Other than that, it's your\n typical haunted forest with leafless trees and a cool breeze")
            note = input(">>>")
            if note == "Note" or "note":
                print("Lmao I took all ur stuuuuuuufff! good luck catching me~\nPS. Ur fat")
                note = 1
                move_number += 1
                continue
            elif note == "":
                note = 0
                move_number += 1
        elif move1 == "pray":
            print("The gods don't answer, yes your faith doesn't waiver\n Faith increased!\n(If you pray at certain times, your faith\nincreases and when your faith increases,\nyour prayers are more likely to be answered")
            faith = 0
            faith += 1
            move_number += 1
            continue
        if move1 == '':
            print("Try to 'pray', 'look around', or 'help'")
            move_number += 1
            continue
      

if __name__ == "__main__":
    start = input("Press enter to get intro")
    print("Hello! Welcome to my first actual game!\nThis is called RPG adventute and was first made in ISS on Febuary 5th, 2020.\nThis is an oddly meta game about you, the player.\nYour whole world is based around extreme rpg and with it on your side,\ncan unlock hidden abilities within yourself and everything around you.\nGood luck traveler, You're going to need it... \n")
    for i in range(5):
        q1 = input("Would you like a guide? Yes or No \n")
        if q1 == "yes":
            guide = input("Okay so here's how you play. Most times, you can go in the 4 cardinal directionsand no matter where you are, you can try to 'look around', 'pray', 'break',\n'use (item)', or other things said in game! At the beginning, try typing 'help' to see your class assigned based on your beginning stats! For any other questions or a more detailed guide, go here: 'Link goes here self' There wont be any walkthroughs seeing how rpg can change the story (Press enter)")
            start2 = input("\nPress anything to start the game!")
            main()
            break
        elif q1 =='no':
            print("Alright well if thats what you want..\n")
            main()
            break
        else:
            print("Come again?\n")
            continue
    if i == 4:
        print("Remember, this game will be case sensitive so type the whole words in lowercase like 'yes' or 'no' or 'help'. please start over")
    
    
        
    
