def game():
    print("Welcome to the game!")
    print("You wake up in a dark and moist forest. You see two paths ahead.")
    choice = input("What path shall ye choose,  portside  (1) or starboard (2)? ")
    
    if choice == "1":
        port()
    elif choice == "2":
        starboard()
    else:
        print("ARRRRRR WRONG CHOICE. Walk the plank.")
        game()  

def port():
    print("Arr matey, you have chosen the dreaded path. A path of mystery!")
    print("You walk forward and see a mysterious figure.")
    choice = input("Do you talk to them (1) or run away (2)? ")
    
    if choice == "1":
        print("You see a pirate, a strange pirate. He seems nice, you follow him.")
        print("He leads you to a strange place.")
        print("You see a strange boat.")
        print("He says: Arr mehatly join me to go on an adventure of a lifetime!")
        choice2 = input("Do you go with him (1) or try to get home (2)? ")
        
        if choice2 == "1":
            print("Pirate: Ah, so you decided to join me on my travels. Adventure awaits!")
            print("Arr, it's me Luigi. Narrator: You get transferred to another universe, a universe where everything is Mario! Creepy, am I right?")
            # add stuff here
        elif choice2 == "2":
            print("You decide to go home. The pirate vanishes, and you find yourself back in the forest.")
        else:
            print("Invalid choice! Try again.")
            port()  # Restart
    elif choice == "2":
        print("You run away, escaping the mysterious figure. The forest grows darker as you wander aimlessly.")
        # 
    else:
        print("Invalid choice! Try something else, pirate.")
        port()  # Restart
def starboard():
    print("You chose the starboard path. A sunny beach awaits. A treasure map lies in the sand!")
    
# Start this shit
game()
