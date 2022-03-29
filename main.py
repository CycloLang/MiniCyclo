import os,sys
import Core.main as mc


VERSION = "0.0.0"

def main(args:list) -> None:

    if len(args) < 2:
        print("Usage: main.py <source file> <optional arguments> <flags>")

    elif "-v" in args:
        print(f"Current version {VERSION}")

    elif "-h" in args:
        print("Usage: main.py <source file> <optional arguments> <flags>")
        print("Flags:")
        print("    -h help")
        print("    -v version")

    else:
        if os.path.exists(args[1]):
            f = open(args[1])
            progArgs = args[2:]    #create a list of arguments to pass to the program
            mc.runFile(f,progArgs)
            f.close()
        else:
            print(f"ERROR: file {args[1]} not found")

if __name__ == "__main__":
    main(sys.argv)