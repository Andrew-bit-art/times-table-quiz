"""Times table quiz: choose a table from 1 to 12, answer the questions, see your score."""


def get_int(prompt):
    """Keep asking until the user types a whole number."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")


def main():
    while True:
        score = 0

        while True:
            table = get_int("Choose a times table (1-12): ")
            if 1 <= table <= 12:
                break
            print("That's not between 1 and 12.")

        total = 12
        for number in range(1, total + 1):
            answer = get_int(f"{table} x {number} = ")
            if answer == table * number:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong, the correct answer is {table * number}.")

        print(f"You scored {score} out of {total}.")

        play_again = input("Play again? (y/n) ").strip().lower()
        if play_again != "y":
            break

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
    """Times table quiz: choose a table from 1 to 12, answer the questions, see your score."""


def get_int(prompt):
    """Keep asking until the user types a whole number."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")


def main():
    while True:
        score = 0

        while True:
            table = get_int("Choose a times table (1-12): ")
            if 1 <= table <= 12:
                break
            print("That's not between 1 and 12.")

        total = 12
        for number in range(1, total + 1):
            answer = get_int(f"{table} x {number} = ")
            if answer == table * number:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong, the correct answer is {table * number}.")

        print(f"You scored {score} out of {total}.")

        play_again = input("Play again? (y/n) ").strip().lower()
        if play_again != "y":
            break

    print("Thanks for playing!")


if __name__ == "__main__":
    main()