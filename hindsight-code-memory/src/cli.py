import argparse, sys
sys.path.insert(0, ".")
from src.indexer import index_folder
from src.agent import ask_agent

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CodeMemory with Hindsight")
    sub = parser.add_subparsers(dest="cmd")

    p_index = sub.add_parser("index")
    p_index.add_argument("folder", help="Path to code folder to index")
    p_index.add_argument("--bank", default="my-codebase")

    p_ask = sub.add_parser("ask")
    p_ask.add_argument("question", help="Question about codebase")
    p_ask.add_argument("--bank", default="my-codebase")

    args = parser.parse_args()
    if args.cmd == "index":
        index_folder(args.folder, args.bank)
    elif args.cmd == "ask":
        ans = ask_agent(args.question, args.bank)
        print(ans)
    else:
        parser.print_help()
