import sys
import os
from Skills.mirror.mirror import MirrorSkill

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        clear_screen()
        print("="*40)
        print(" 🏛️  GEMINI-CORE CENTRAL HUB (v3.0) ")
        print("="*40)
        print("1. 🪞 Run Mirror Sync (C: -> H:)")
        print("2. 💼 Launch Job-Hunter CLI")
        print("3. 🧱 Launch Lego-Collector")
        print("4. 🧠 Launch Citable-RAG")
        print("5. 📊 System Status & Git Sync")
        print("q. 🚪 Exit")
        print("-"*40)
        
        choice = input("Select an option: ").lower()
        
        if choice == '1':
            print("\nTriggering mirror...")
            mirror = MirrorSkill()
            mirror.mirror_all()
            input("\nPress Enter to return to menu...")
        elif choice == '2':
            print("\nLaunching Job-Hunter...")
            os.system("python Projects/Job-Hunter-CLI/engine/job_hunter.py") 
        elif choice == '3':
            print("\nLaunching Lego-Collector...")
            os.system("python Projects/Lego-Collector/engine/brickset_tool.py")
        elif choice == '4':
            print("\nLaunching Citable-RAG...")
            # os.system("python Projects/Citable-RAG/main.py")
            print("Feature coming soon!")
            input("\nPress Enter...")
        elif choice == '5':
            print("\nChecking Git status...")
            os.system("git status")
            input("\nPress Enter to return to menu...")
        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
            input("\nPress Enter...")

if __name__ == "__main__":
    main_menu()
