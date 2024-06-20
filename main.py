import random

def main():
    random.seed()
    val = random.randint(0,9)

    strategies = ["Look for any word or phrase","Work in silence",
                  "Look at you hand and count down from five, say an idea",
                  "Use physical tools","Must include X","Random image",
                  "Describe an idea in one sentence, go from there",
                  "Create with the fewest possible parts",
                  "Collaborate, alternate contributing elements",
                  "No editing"
                  ]

    print("- Constraint challenge -\n")
    input("Press any key to continue\n")
    print("Your constraint: ")
    print(strategies[val])
    
main()
