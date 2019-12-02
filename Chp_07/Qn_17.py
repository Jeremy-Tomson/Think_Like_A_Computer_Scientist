# Q17
# a)
# b)
# c)
# d)


def play_once(human_plays_first):
    """
       Must play one round of the game. If the parameter
       is True, the human gets to play first, else the
       computer gets to play first.  When the round ends,
       the return value of the function is one of
       -1 (human wins),  0 (game drawn),   1 (computer wins).
    """
    # This is all dummy scaffolding code right at the moment...
    import random                  # See Modules chapter ...
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1,2)
    # print("Human plays first={0},  winner={1} " # .format(human_plays_first, result))
    return result


def play_game():
    q = input("Do you want to play a game?")
    p1 = 0
    p2 = 0
    d = 0
    g = 0
    while q == "Yes":
        for i in (True, False):
            outcome = play_once(i)
            if outcome == -1:
                p1 += 1
                g += 1
                if p1 <= 0:
                    percentage_won = 0
                else:
                    percentage_won = (p1/g)*100
                print("You Win!", "\n", "Your Score:", p1, "\n", "My Score:", p2, "\n", "Draws:", d, "You won ", int(float(percentage_won)), "% of all games played!")
                n = input("Do you want to play again?")

            elif outcome == 0:
                d += 1
                g += 0
                if p1 <= 0:
                    percentage_won = 0
                else:
                    percentage_won = (p1/g)*100
                print("It's A Draw!", "\n", "Your Score:", p1, "\n", "My Score:", p2, "\n", "Draws:", d, "You won ", int(float(percentage_won)), "% of all games played!")
                n = input("Do you want to play again?")

            elif outcome == 1:
                p2 += 1
                g += 1
                if p1 <= 0:
                    percentage_won = 0
                else:
                    percentage_won = (p1/g)*100
                print("I Win!", "\n", "Your Score:", p1, "\n", "My Score:", p2, "\n", "Draws:", d, "You won ", int(float(percentage_won)), "% of all games played!")
                n = input("Do you want to play again?")

    else:
        print("Goodbye!")
    return


play_game()
