import random

def main():
    random.seed()
    val = random.randint(0,9)

    f = open("strategies.txt", "r")

    strategies = f.readlines()
    print("- Constraint challenge -\n")
    input("Press any key to continue\n")
    print("Your constraint: ")
    print(strategies[val])
    
main()
