#Lela Parks
#Dec 2, 2024
#Chapter 3

#Tasks at hand for Billy

#1 Ask For Directions
#2 Find Food
#3 Jump

#Code will give player the option to find food,jump, and ask for directionns

#Ask For Directions
#Jump
#Find Food

import random
import math

# Initialize global variables
tracks = 0  # Start with 0 tracks
points = 4  # Points or other bonuses could be used here (not really in use for now)
energy = 25  # Starting energy
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
energy = 25  # Starting energy
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

# Gameplay choices function
def gameplay_choice():
    print("\nWhat do you want to do?")
    print("1. Ask for directions")
    print("2. Find food")
    print("3. Jump")
    print("4. Rest (Gain some energy but lose time)")

    choice = input("> ")
    if choice == "1":
        ask_for_directions()
    elif choice == "2":
        find_food()
    elif choice == "3":
        jump()
    elif choice == "4":
        rest()
    else:
        print("Invalid choice. Please choose again.")
        gameplay_choice()

def npc_interaction():
    npc_names = ["Owl", "Elk", "Snow-Quail", "Bison"]
    responses = ["Hi there", "Are you lost?", "I can help you!"]

    npc_name = random.choice(npc_names)
    print(f"{npc_name}: Hello, I am {npc_name}. Would you like to talk to me? (y/n)")

    choice = input("> ").lower()
    if choice == "y":
        print(f"{npc_name}: {random.choice(responses)}")
    else:
        print(f"{npc_name}: Goodbye.")

# Actions: ask for directions
def ask_for_directions():
    print("You ask a nearby animal for directions.")
    # Random chance of directions being helpful
    success = random.random() < 0.7  # 70% chance for directions to be helpful
    if success:
        print("The directions were helpful!")
        manage_energy_and_time(5, 10)  # Costs 5 energy, 10 seconds of time
    
    else:
        print("The directions were confusing and wasted your time!")
        manage_energy_and_time(10, 15)  # Costs 10 energy, 15 seconds of time

# Actions: find food
def find_food():
    global tracks
    print("You search for food in the nearby woods.")
    food_found = random.random() < 0.8  # 80% chance to find food
    if food_found:
        print("You found some food!")
        manage_energy_and_time(5, 15)  # Costs 5 energy, 15 seconds of time
        tracks += 3  # Gain 3 tracks for finding food
    else:
        print("You couldn't find any food.")
        manage_energy_and_time(10, 10)  # Costs 10 energy, 10 seconds of time

# Actions: jump
def jump():
    global tracks
    print("You attempt to jump over an obstacle.")
    success = random.random() < 0.6  # 60% chance to succeed at the jump
    if success:
        print("You successfully jumped over the obstacle!")
        manage_energy_and_time(10, 5)  # Costs 10 energy, 5 seconds of time
        tracks += 6  # Gain 6 tracks for success
    else:
        print("You tripped! That was a failed jump.")
        manage_energy_and_time(15, 5)  # Costs 15 energy, 5 seconds of time

# Actions: rest (recover energy but lose time)
def rest():
    global energy, time
    print("You decide to rest and recover some energy.")
    energy_recovered = math.floor(random.uniform(5, 10))  # Recover between 5 to 10 energy
    time_lost = 10  # Resting costs 10 seconds
    energy += energy_recovered
    time -= time_lost
    print(f"You regained {energy_recovered} energy, but you lost {time_lost} seconds.")

# Start game
def start_game():
    global tracks
    print("Game Starting...")
    print("Level 4: Explore Lower Alpine Zone.")
    
    while energy > 0 and time > 0:  # Keep playing while there's time and energy
        gameplay_choice()  # Start gameplay decisions for the first level
        print(f"Tracks: {tracks} | Energy: {energy} | Time left: {time} seconds.")
        
        # Check if the player has enough tracks to proceed
        if tracks >= 15:
            print("Congratulations, you’ve completed The Lower Alpine Zone.")
            proceed_to_level_4()
            break  # End the loop if the player proceeds to level 4

    if energy <= 0 or time <= 0:
        print("Game Over. You ran out of energy or time.")
        exit()

# Proceed to next level
def proceed_to_level_4():
    print("Congratulations, you’ve completed The Subalpine Zone!")
    print("Proceeding to Level 4...")
    # Start next level gameplay logic or end game here
    # For now, let's end the game after this level

# Boolean function to check if player can proceed
def check_can_proceed():
    # Example of unique logic with boolean check
    return tracks >= 15 and energy > 0 and time > 0  # Must have enough tracks, energy, and time

# Start the game with the title screen
title_screen()  # This will start the game when the script is run
