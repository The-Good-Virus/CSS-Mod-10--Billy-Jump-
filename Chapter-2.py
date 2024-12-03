#Lela Parks
#Nov 9, 2024
#Chapter 2

#Tasks at hand for Billy

#1 Ask For Directions
#2 Find Food
#3 Jump

#Code will give player the option to find food,jump, and ask for directionns

#Ask For Directions
#Jump
#Find Food

import random

# Initialize global variables
tracks = 0  # Start with 0 tracks
points = 8  # Points or other bonuses could be used here (not really in use for now)
energy = 75  # Starting energy
time = 60  # Starting time in seconds

def title_screen():
    print("Welcome to Billy Jump!")
    print("Press 'Enter' to start or 'q' to quit.")
    choice = input("> ").lower()
    if choice == "":  # This checks if the user pressed Enter (empty string)
        start_game()
    elif choice == "q":
        print("Goodbye!")
        exit()
    else:
        print("Invalid input. Please try again.")
        title_screen()

# Initialize energy and time
energy = 75  # Starting energy
time = 60     # Starting time in seconds

def manage_energy_and_time(action_cost, time_cost):
    global energy, time
    
    energy -= action_cost
    time -= time_cost
    
    if energy <= 0:
        print("You have no energy left! Game Over.")
        exit()
    elif time <= 0:
        print("Time's up! You failed to complete the quest.")
        exit()
    else:
        print(f"Energy: {energy} | Time remaining: {time} seconds.")

def gameplay_choice():
    print("\nWhat do you want to do?")
    print("1. Ask for directions")
    print("2. Find food")
    print("3. Jump")

    choice = input("> ")
    if choice == "1":
        ask_for_directions()
    elif choice == "2":
        find_food()
    elif choice == "3":
        jump()
    else:
        print("Invalid choice. Please choose again.")
        gameplay_choice()

def npc_interaction():
    npc_names = ["Owl", "Elk", "Snow-Quail", "Bison"]
    responses = ["Hi there", "Are you lost?", "I can help you!"]
    
    # Choose a random NPC
    npc_name = random.choice(npc_names)
    
    # Random chance (50%) for NPCs to know the way
    knows_directions = random.choice([True, False])  # 50% chance they know the way
    
    print(f"{npc_name}: Hello, I am {npc_name}. Would you like to talk to me? (y/n)")
    
    choice = input("> ").lower()
    if choice == "y":
        if knows_directions:
            print(f"{npc_name}: Sure, I can help you with directions!")
            # Here you can insert specific directions or some help logic
            print("You now know where to go!")
            manage_energy_and_time(5, 5)  # NPC help costs 5 energy and 5 time
        else:
            print(f"{npc_name}: Sorry, I don’t know the way.")
            # No directions, but maybe the NPC can give some generic advice
            print(f"{npc_name}: Maybe try asking someone else.")
            manage_energy_and_time(5, 5)  # Still costs time and energy to ask
    else:
        print(f"{npc_name}: Goodbye.")

def ask_for_directions():
    print("You ask a nearby animal for directions.")
    npc_interaction()  # Let NPCs decide if they know the way or not
    manage_energy_and_time(5, 10)  # Costs 5 energy, 10 seconds of time

def find_food():
    global tracks  # Increase tracks if food is found
    print("You search for food in the nearby woods.")
    # Logic for finding food or facing consequences
    manage_energy_and_time(10, 20)  # Costs 10 energy, 20 seconds of time
    tracks += 6  # Gain 6 track for finding food

def jump():
    global tracks  # Increase tracks if food is found
    print("You attempt to jump over an obstacle.")
    # Logic for jumping or failure consequences
    tracks += 7  # Gain 7 track for finding food
    manage_energy_and_time(15, 5)  # Costs 15 energy, 5 seconds of time

def start_game():
    global tracks  # To access the global `tracks` variable
    print("Game Starting...")
    print("Level 2: Explore the Montane Zone.")
    
    while energy > 0 and time > 0:  # Keep playing while there's time and energy
        gameplay_choice()  # Start gameplay decisions for the first level
        print(f"Tracks: {tracks} | Energy: {energy} | Time left: {time} seconds.")
        
        # Check if the player has enough tracks to proceed
        if tracks >= 20:
            proceed_to_level_3()
            break  # End the loop if the player proceeds to level 2

    if energy <= 0 or time <= 0:
        print("Game Over. You ran out of energy or time.")
        exit()

def proceed_to_level_3():
    print("Congratulations, you’ve completed The Montane Zone!")
    print("Proceeding to Level 3...")
    # Start next level gameplay logic
    # You can add more levels, new objectives, or just end the game here.

title_screen()  # This will start the game when the script is run