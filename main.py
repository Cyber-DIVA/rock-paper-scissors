import random
import os
import time

handArt1 = """\n
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

handArt2 = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

handArt3 = """\n
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

handArt4 = """\n
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)\n"""

handArt5 = """\n
    _______
---'   ____)____
          ______)
          _______)
          _______)
---.__________)\n"""

handArt6 = """\n
    _______
---'   ____)____
          ______)
        __________)
      (____)
---.__(___)\n"""

art1 = """\n
\t\t\t\t\t\t\t        _      _                   
\t\t\t\t\t\t\t       (_)    | |                  
\t\t\t\t\t\t\t __   ___  ___| |_ ___  _ __ _   _ 
\t\t\t\t\t\t\t \ \ / / |/ __| __/ _ \| '__| | | |
\t\t\t\t\t\t\t  \ V /| | (__| || (_) | |  | |_| |
\t\t\t\t\t\t\t   \_/ |_|\___|\__\___/|_|   \__, |
 \t\t\t\t\t\t\t                             __/ |
  \t\t\t\t\t\t\t                          |___/ \n"""

art2 = """\n
\t\t\t\t\t\t\t _______  _______ __________________ _______  _       __________________          _ 
\t\t\t\t\t\t\t(  ____ \(  ___  )\__   __/\__   __/(  ___  )( \      \__   __/\__   __/|\     /|( )
\t\t\t\t\t\t\t| (    \/| (   ) |   ) (      ) (   | (   ) || (         ) (      ) (   ( \   / )| |
\t\t\t\t\t\t\t| (__    | (___) |   | |      | |   | (___) || |         | |      | |    \ (_) / | |
\t\t\t\t\t\t\t|  __)   |  ___  |   | |      | |   |  ___  || |         | |      | |     \   /  | |
\t\t\t\t\t\t\t| (      | (   ) |   | |      | |   | (   ) || |         | |      | |      ) (   (_)
\t\t\t\t\t\t\t| )      | )   ( |___) (___   | |   | )   ( || (____/\___) (___   | |      | |    _ 
\t\t\t\t\t\t\t|/       |/     \|\_______/   )_(   |/     \|(_______/\_______/   )_(      \_/   (_)\n"""






clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

print("\nHello! Ready to play some Rock, Paper, Scissors ( ͡❛‿‿ ͡❛) ?!\n"
      "Let's go! ٩( ᐛ )و \n")


action = ["rock", "paper", "scissors"]

myAction = ""
computerAction = ""

def hands():
    if myAction == action[0]:
        print(handArt4)
    elif myAction == action[1]:
        print(handArt5)
    else:
        print(handArt6)



def rules(myAction, computerAction):
    if myAction == computerAction:
        print("Draw!")
    elif myAction == action[0] and computerAction == action[2] or myAction == action[1] and computerAction == action[0] or myAction == action[2] and computerAction == action[1]:
        print("You Win!\n" + art1)
    else:
        print("Computer Wins!\n" + art2)

def computer():
    global computerAction
    computerAction = random.choice(action)
    clearConsole()
    hands()
    print(handArt1)
    time.sleep(0.5)
    clearConsole()
    hands()
    print(handArt2)
    time.sleep(0.5)
    clearConsole()
    hands()
    print(handArt3)
    time.sleep(0.5)
    clearConsole()
    hands()
    time.sleep(0.8)
    if computerAction == action[0]:
        print(handArt4)
    elif computerAction == action[1]:
        print(handArt5)
    else:
        print(handArt6)
    print("Computer chose: {}".format(computerAction))

while True:
    while myAction not in action:
        x = input("Enter a valid choice: ").strip().lower()
        clearConsole()
        myAction = x
        if myAction in action:
            print("You choose: " + x)
            hands()
            computer()
            rules(myAction, computerAction)
            myAction = ""
            break
        else:
            print("Try again!")
            break




















