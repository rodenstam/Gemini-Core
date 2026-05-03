import argparse
import sys
import os
from logic import LibrarianLogic

def main():
    parser = argparse.ArgumentParser(description="Gemini-Core Librarian CLI")
    subparsers = parser.add_subparsers(dest="command", help="Kommandon")

    # Audit command
    audit_parser = subparsers.add_parser("audit", help="Granska systemet för fel")
    
    # Archive command
    archive_parser = subparsers.add_parser("archive", help="Arkivera en plan")
    archive_parser.add_argument("plan_file", help="Namn på plan-filen i Strategy/ eller Plans/")

    # Tidy command
    tidy_parser = subparsers.add_parser("tidy", help="Fullständig systemstädning med förslag")

    # Fix command
    fix_parser = subparsers.add_parser("fix", help="Auto-fixar kända problem (t.ex. datum-prefix i arkivet)")

    args = parser.parse_args()
    
    # Root dir calculation
    root_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
    librarian = LibrarianLogic(root_dir)

    if args.command == "audit":
        librarian.run_audit()
    elif args.command == "archive":
        librarian.archive_plan(args.plan_file)
    elif args.command == "tidy":
        librarian.run_tidy()
    elif args.command == "fix":
        librarian.run_fix()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
