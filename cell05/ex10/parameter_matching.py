from sys import argv

def main():
    if len(argv) != 2:
        print("none")
        return

    keyword = argv[1]
    word = input("What was the parameter? ")

    if word == keyword:
        print("Good job!")
    else:
        print("Nope, sorry...")

main()