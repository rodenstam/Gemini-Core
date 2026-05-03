import argparse
import sys
from crawler import Crawler
from search_engine import SearchEngine

def main():
    parser = argparse.ArgumentParser(description="Gemini-Core Semantic Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Kommandon")

    # Index command
    index_parser = subparsers.add_parser("index", help="Indexera hela systemet")
    index_parser.add_argument("--root", default=".", help="Rotmapp att indexera")
    index_parser.add_argument("--silent", action="store_true", help="Kör utan output")

    # Search command
    search_parser = subparsers.add_parser("search", help="Sök i systemet")
    search_parser.add_argument("query", help="Din sökfråga")
    search_parser.add_argument("--top", type=int, default=5, help="Antal resultat")

    args = parser.parse_args()

    if args.command == "index":
        crawler = Crawler(args.root)
        crawler.index_all(silent=args.silent)
    elif args.command == "search":
        engine = SearchEngine()
        results = engine.search(args.query, top_n=args.top)
        
        if not results:
            print("Inga resultat hittades eller sökningen misslyckades.")
            return

        print(f"\n🔎 Topp {len(results)} resultat för: '{args.query}'\n")
        print("-" * 60)
        for i, r in enumerate(results, 1):
            print(f"{i}. [{r['score']:.4f}] {r['path']}")
            print(f"   💡 {r['summary']}\n")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
