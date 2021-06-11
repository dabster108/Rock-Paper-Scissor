import random

def Choosing_Option():
    person_input = input("Choose Rock, Paper or Scissors: ")
    if person_input in ["Rock", "rock", "r", "R"]:
        person_input = "r"
    elif person_input in ["Paper", "paper", "p", "P"]:
        person_input = "p"
    elif person_input in ["Scissors", "scissors", "s", "S"]:
        person_input= "s"
    else:
        print("I can't understand , try again.")
        Choosing_Option()
    return person_input

def Comp_Option():
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    else:
        comp_choice = "s"
    return comp_choice


while True:
    print("")
    
    person_input = Choosing_Option()
    comp_choice = Comp_Option()

    print("")
    
    if person_input == "r":
        if comp_choice == "r":
            print("You chose rock. The computer chose rock. You tied.")
        
        elif comp_choice == "p":
            print("You chose rock. The computer chose paper. You lose.")
          
            
        elif comp_choice == "s":
            print("You chose rock. The computer chose scissors. You win.")
           
    elif person_input == "p":
        if comp_choice == "r":
            print("You chose paper. The computer chose rock. You win.")
          
        
        elif person_input == "p":
            print("You chose paper. The computer chose paper. You tied.")
            
            
        elif comp_choice == "s":
            print("You chose paper. The computer chose scissors. You lose.")
            

    elif person_input == "s":
        if comp_choice == "r":
            print("You chose scissors. The computer chose rock. You lose.")
            
        
        elif comp_choice == "p":
            print("You chose scissors. The computer chose paper. You win.")
            
            
        elif comp_choice == "s":
            print("You chose scissors. The computer chose scissors. You tied.")

    print("")
    print("")
    
    person_input = input("Do you want to play again? (y/n)")
    if person_input in ["Y", "y", "yes", "Yes"]:
        pass
    elif person_input in ["N", "n", "no", "No"]:
        break
    else:
        break
