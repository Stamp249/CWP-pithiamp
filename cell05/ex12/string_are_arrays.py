from sys import argv

def main():
    if not len(argv) > 1:
        print("none")
        return
    keyword = argv[1]
    tmp = ""
    for i in keyword:
        if i == "z":
            tmp+= "z"
    if not tmp:
        print("none")
    else:
        print(tmp)

main()