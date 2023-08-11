MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit"""


def main():
    score = ''
    print(MENU)
    choice = input("choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            if score == '':
                print('missing value')
            else:
                print(determine_status(score))
        elif choice == "S":
            if score == '':
                print('missing value')
            else:
                print('*' * score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("choice: ").upper()
    print("farewell.")


def determine_status(score2):
    """Determine the status of the score."""
    if score2 < 0 or score2 > 100:
        return "Invalid score"
    elif score2 >= 90:
        return "Excellent"
    elif score2 >= 50:
        return "Passable"
    else:
        return "Bad"


def get_valid_score():
    score1 = int(input('score:'))
    while not(score1 >= 0 and score1 <= 100):
        print('invalid score')
        score1 = int(input('score:'))
    return score1


main()
