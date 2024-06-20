choice = "-"
# valid = {"1", "2", "3", "4", "5"}
while choice != "0":
    print(set("12345"))
    if choice in {"1", "2", "3", "4", "5"}:  # or valid // set("12345") slower due to calling set function each time around the loop
        print("You chose {}".format(choice))
    else:
        print("Please choose your option below:")
        print("1:\tLearn Python")
        print("2:\tLearn Python")
        print("3:\tLearn Python")
        print("4:\tLearn Python")
        print("5:\tLearn Python")
        print("0:\tExit")

    choice = input()
