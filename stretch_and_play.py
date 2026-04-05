import random
import time
import os

# Mild gymnast activities
basic_activities = [
    "Stretch your arms high and reach for the ceiling",
    "Balance on one foot for 10 seconds",
    "Do 5 slow squats with arms extended",
    "Hop lightly in place 10 times",
    "Touch your toes slowly 5 times"
]

medium_activities = [
    "Do 10 gentle lunges alternating legs",
    "Pretend to walk a tightrope across the room",
    "Roll your shoulders and neck for 30 seconds",
    "Do 5 seated twists to stretch your back",
    "Step side-to-side like a slow dance"
]

chaos_activities = [
    "Hop on one foot while narrating what you’re doing",
    "Stretch arms while making silly faces",
    "Do gentle squats while humming a song",
    "Pretend to tiptoe across an invisible balance beam",
    "March in place like a marching band conductor"
]

# Cheer animation
cheers = [
    "👏 Nice move!",
    "🤸 Great balance!",
    "🎉 Keep it up!",
    "😎 Smooth and steady!"
]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def start_screen():
    clear()
    print("===================================")
    print("      🤸‍♂️ STRETCH & PLAY 🤸‍♀️       ")
    print("===================================")
    print("Press Enter to start your gentle gymnastics fun...")
    input()

def get_challenge(level):
    if level == 1:
        return random.choice(basic_activities)
    elif level == 2:
        return random.choice(basic_activities + medium_activities)
    else:
        return random.choice(medium_activities + chaos_activities)

def show_cheer():
    print("\n" + random.choice(cheers) + "\n")
    time.sleep(1.5)

def main():
    start_screen()
    round_number = 1
    level = 1
    score = 0
    try:
        while True:
            clear()
            print(f"🔥 Round {round_number} 🔥")
            print(f"🏆 Score: {score}")
            challenge = get_challenge(level)
            print(f"\n🤸 Your challenge: {challenge}\n")
            
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
            
            # Adjust level and score based on boredom
            score += 6 - boredom  # higher boredom = more challenging, less score
            if boredom <= 2:
                level = 1
            elif boredom <= 4:
                level = 2
            else:
                level = 3
                print("💥 FUN MODE ACTIVATED! Gentle challenge ahead! 💥")
            
            show_cheer()
            round_number += 1
            time.sleep(2)
    except KeyboardInterrupt:
        clear()
        print("🎮 Game over! 🎮")
        print(f"🏅 Total rounds completed: {round_number-1}")
        print(f"🏆 Final Score: {score}")
        print("🤸‍♂️ Hope your boredom is gently stretched away! 🤸‍♀️")

if __name__ == "__main__":
    main()
