import random
import time
import os

# Activities
basic_activities = [
    "Make a hot chocolate and watch a silly video",
    "Draw a tiny comic about a squirrel spy",
    "Text a friend something totally ridiculous",
    "Learn a tongue twister and master it",
    "Try a 3-minute dance challenge",
]

medium_activities = [
    "Make a meme about your day",
    "Write a fake ad for a useless invention",
    "Pretend you are a secret agent and spy on your own room",
    "Invent a new handshake for yourself",
    "Do 10 pushups while singing your favorite song"
]

chaos_effects = [
    "while hopping on one foot",
    "while wearing sunglasses indoors",
    "while speaking like a pirate",
    "while narrating every move out loud",
    "blindfolded (just kidding, maybe not!)",
    "while doing your best villain laugh"
]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def start_screen():
    clear()
    print("===================================")
    print("       🌀 BOREDOM BUSTER 🌀        ")
    print("===================================")
    print("Press Enter to start the madness...")
    input()

def get_challenge(level):
    if level == 1:
        return random.choice(basic_activities)
    elif level == 2:
        return random.choice(basic_activities + medium_activities)
    else:
        return random.choice(medium_activities) + " " + random.choice(chaos_effects)

def main():
    start_screen()
    round_number = 1
    level = 1
    try:
        while True:
            clear()
            print(f"🔥 Round {round_number} 🔥")
            challenge = get_challenge(level)
            print(f"\n🎉 Your challenge: {challenge}\n")
            
            # Ask user for boredom rating
            while True:
                try:
                    boredom = int(input("Rate your boredom after this (1 = chill, 5 = desperate): "))
                    if 1 <= boredom <= 5:
                        break
                    else:
                        print("Please enter a number between 1 and 5.")
                except ValueError:
                    print("Enter a number between 1 and 5!")
            
            # Adjust level based on boredom
            if boredom <= 2:
                level = 1
            elif boredom <= 4:
                level = 2
            else:
                level = 3
                print("💥 CHAOS MODE ACTIVATED! 💥 Next challenge will be wild...")
            
            print("😎 Get ready for the next challenge...")
            round_number += 1
            time.sleep(3)
    except KeyboardInterrupt:
        print("\n🎮 Game over! Hope your boredom is annihilated! 🎮")

if __name__ == "__main__":
    main()
