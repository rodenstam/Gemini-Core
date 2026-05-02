import sys
import os
import subprocess
from Skills.mirror.mirror import MirrorSkill

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        clear_screen()
        print("="*40)
        print(" 🏛️  GEMINI-CORE CENTRAL HUB (v4.0) ")
        print("="*40)
        print("1. 🛡️ System Health Audit (with Mirror)")
        print("2. 🪞 Manual Mirror Sync (C: -> H:)")
        print("3. 💼 Launch Job-Hunter CLI")
        print("4. 🧱 Launch Lego-Collector")
        print("5. 🧠 Launch Citable-RAG")
        print("6. 📊 Git Status")
        print("q. 🚪 Exit")
        print("-"*40)
        
        choice = input("Select an option: ").lower()
        
        if choice == '1':
            print("\nRunning System Auditor...")
            # Run auditor with --mirror flag
            os.system(f"{sys.executable} Shared/auditor.py --mirror")
            input("\nAudit complete. Press Enter to return to menu...")
        elif choice == '2':
            print("\nTriggering Manual Mirror...")
            mirror = MirrorSkill()
            mirror.mirror_all()
            input("\nPress Enter to return to menu...")
        elif choice == '3':
            print("\nLaunching Job-Hunter...")
            os.system(f"{sys.executable} Projects/Job-Hunter-CLI/engine/job_hunter.py") 
            input("\nPress Enter to return to menu...")
        elif choice == '4':
            print("\nLaunching Lego-Collector...")
            os.system(f"{sys.executable} Projects/Lego-Collector/engine/brickset_tool.py")
            input("\nPress Enter to return to menu...")
        elif choice == '5':
            print("\nLaunching Citable-RAG...")
            rag_entry = "Projects/Citable-RAG/main.py"
            if os.path.exists(rag_entry):
                os.system(f"{sys.executable} {rag_entry}")
            else:
                print("Error: Citable-RAG entry point not found.")
            input("\nPress Enter...")
        elif choice == '6':
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
