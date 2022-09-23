import time
import random
import os


def clear():
    # clears the console
    # used for keeping output clean

    _ = os.system('cls')

def loading():
    # a loading bar animation

    print("\n[", end="")

    for _ in range(0, 25):
        x = random.choice([0.05, 0.07, 0.1 ])
        time.sleep(x)
        print("█", end="", flush=True)

    print("]")

def welcome():
    print(r'''    .                  .-.    .  _   *     _   .
           *          /   \     ((       _/ \       *    .
         _    .   .--'\/\_ \     `      /    \  *    ___
     *  / \_    _/ ^      \/\'__        /\/\  /\  __/   \ *
       /    \  /    .'   _/  /  \  *' /    \/  \/ .`'\_/\   .
  .   /\/\  /\/ :' __  ^/  ^/    `--./.'  ^  `-.\ _    _:\ _
     /    \/  \  _/  \-' __/.' ^ _   \_   .'\   _/ \ .  __/ \
   /\  .-   `. \/     \ / -.   _/ \ -. `_/   \ /    `._/  ^  \
  /  `-.__ ^   / .-'.--'    . /    `--./ .-'  `-.  `-. `.  -  `.
@/        `.  / /      `-.   /  .-'   / .   .'   \    \  \  .-  \%
@&8jgs@@%% @)&@&(88&@.-_=_-=_-=_-=_-=_.8@% &@&&8(8%@%8)(8@%8 8%@)%
@88:::&(&8&&8:::::%&`.~-_~~-~~_~-~_~-~~=.'@(&%::::%@8&8)::&#@8::::
`::::::8%@@%:::::@%&8:`.=~~-.~~-.~~=..~'8::::::::&@8:::::&8:::::'
 `::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::.'

                    {tiny text adventure}
            ''')

def main():
    while True:
        choose = input("Are you ready to play? (y/n): ")
        if choose == 'y':
            print("Awesome! Let's go!")

            loading()
            clear()
            welcome()

            print("You are wandering around in a jungle, close to where you set camp.")
            time.sleep(3)
            print("It has been 5 hours since you lost your way...")
            time.sleep(3)
            print("It's pitch darkness all around with the occassional howls of wolves and creepy footsteps...")
            time.sleep(3)
            print("You notice a small light at a distance, turns out it's a cave! You are relieved.")
            time.sleep(3)
            print("As you enter, it's mossy and you can barely make out anything except a stick on the floor.")
            time.sleep(3)

            choose = input("\n// do you take the stick? (y/n): ")

            stick = 0
            time.sleep(1)
            if choose == "y":
                print("\nYou pick the stick, and hold it for later.")
                stick = 1

            else:
                print("\nYou feel suspicous and leave the stick alone.")

            print("As you proceed further into the cave, you see a small glowing object...")
            time.sleep(3)

            choose = input("\n// do you approach the object? (y/n): ")
            time.sleep(1)
            if choose == "y":
                print("\nYou approach the object...")
                time.sleep(3)
                print("As you draw closer, you begin to make out the object as an eye!")
                time.sleep(3)
                print("The eye belongs to a giant mystical spider!")
                time.sleep(3)
                print("The spider looks angry! Ready to fight!")

                choose = input("\n// do you fight the spider? (y/n): ")
                time.sleep(1)
                if choose == "y":
                    print("\nYou choose to fight the spider.")
                    time.sleep(3)

                    if stick == 1:
                        print("You remember the stick and take it out!")
                        time.sleep(3)
                        print("\n================================================")
                        print("                 Fighting Rules                   ")
                        print("   YOU MUST HIT ABOVE A 5 TO KILL THE SPIDER    ")
                        print("IF THE SPIDER HITS HIGHER THAN YOU, YOU WILL DIE")
                        print("================================================")
                        time.sleep(3)
                        fdmg1 = int(random.randint(3, 10))
                        edmg1 = int(random.randint(1, 5))
                        print("you hit a", fdmg1)
                        print("the spider hits a", edmg1)
                        time.sleep(3)

                        if edmg1 > fdmg1:
                            print("The spider has dealt more damage than you!")
                            complete = 0
                            return complete

                        elif fdmg1 < 5:
                            print("You didn't do enough damage to kill the spider, but you manage to escape")
                            complete = 1
                            return complete

                        else:
                            print("You killed the spider!")
                            complete = 1
                            return complete
                    
                    
                    else:
                        print("You don't have anything to fight with!")
                        time.sleep(3)
                        print("You prepare your fists and get ready to fight!")
                        time.sleep(3)
                        print("\n================================================")
                        print("                  Fighting Rules                 ")
                        print("   YOU MUST HIT ABOVE A 5 TO KILL THE SPIDER    ")
                        print("IF THE SPIDER HITS HIGHER THAN YOU, YOU WILL DIE")
                        print("================================================")
                        time.sleep(3)
                        fdmg1 = int(random.randint(1, 8))
                        edmg1 = int(random.randint(1, 5))
                        print("\n// you hit a", fdmg1)
                        print("\n// the spider hits a", edmg1, "\n")
                        time.sleep(3)

                        if edmg1 > fdmg1:
                            print("The spider has dealt more damage than you!")
                            complete = 0
                            return complete

                        elif fdmg1 < 5:
                            print("You didn't do enough damage to kill the spider, but you manage to escape")
                            complete = 1
                            return complete

                        else:
                            print("You killed the spider!")
                            complete = 1
                            return complete

                else:
                    print("\nYou choose not to fight the spider.")
                    time.sleep(3)
                    print("You start turning away quietely...")
                    time.sleep(3)
                    print("The spider ambushes you and impales you with it's fangs!")
                    time.sleep(3)
                    print("You are badly hurt, you try to leave but...")
                    complete = 0
                    return complete
                
                
            else:
                print("\nYou turn away from the glowing object, and attempt to leave the cave...")
                time.sleep(3)
                print("But something won't let you...")
                time.sleep(3)
                print("Turns out the glowing object was a giant mystical spider!")
                time.sleep(3)
                print("It impales you with it's giant claws, you try to leave but...")
                complete = 0
                return complete

        else:
            print("Would've loved to play! Next time perhaps.")
            time.sleep(3)
            complete = 2
            return complete


if __name__ == "__main__":

    complete = main()
    if complete == 1:
        print('You manage to run out of the cave! You won! ^^')
        time.sleep(5)

    elif complete == 0:
        print("You couldn't escape... You have lost. :(")
        time.sleep(5)

    else:
        pass
