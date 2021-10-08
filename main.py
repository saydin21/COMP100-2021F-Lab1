p1 = input("Select Rock(R), Paper(P) or Scissors(S) for player 1")
p2 = input("Select Rock(R), Paper(P) or Scissors(S) for player 2")

if p1 == "R":
    if p2 == "R":
        print("tie")
    elif p2 == "P":
        print("p2 won")
    elif p2 == "S":
        print("p1 won")
    else:
        print("invalid input")
elif p1 == "P":
    if p2 == "R":
        print("p1 won")
    elif p2 == "P":
        print("tie")
    elif p2 == "S":
        print("p2 won")
    else:
        print("invalid input")
elif p1 == "S":
    if p2 == "R":
        print("p1 won")
    elif p2 == "P":
        print("p2 won")
    elif p2 == "S":
        print("tie")
    else:
        print("invalid input")
else:
    print("invalid input")
