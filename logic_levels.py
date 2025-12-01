import random
import textwrap

BANNER = "=" * 60

class Level:
    def __init__(self, number, description, question, answer, hint):
        self.number = number
        self.description = description
        self.question = question
        self.answer = answer
        self.hint = hint
        self.max_attempts = 3

    def play(self):
        print(BANNER)
        print(f"Level {self.number}")
        print(BANNER)
        print(textwrap.fill(self.description, width=70))
        print()
        print(self.question)
        attempts_left = self.max_attempts

        while attempts_left > 0:
            guess = input(f"> Your answer ({attempts_left} attempt(s) left): ").strip()

            # Normalize yes/no answers and simple strings
            if isinstance(self.answer, str):
                is_correct = guess.lower() == self.answer.lower()
            else:
                is_correct = guess == str(self.answer)

            if is_correct:
                print("✅ Correct! Moving to the next level.\n")
                return True

            attempts_left -= 1
            if attempts_left > 0:
                print("❌ Not quite.")
                print(f"HINT: {self.hint}\n")
            else:
                print("❌ Out of attempts.")
                print(f"The correct answer was: {self.answer}\n")
                return False


def make_levels():
    # Level 1: Even/odd logic
    secret = random.choice([12, 18, 24, 32])
    lvl1 = Level(
        number=1,
        description=(
            "You find a locked door with a keypad. A note says: "
            "\"This door only opens for numbers that are even and "
            "divisible by 3, but less than 35.\""
        ),
        question=(
            f"One valid code has already been chosen: {secret}. "
            "Type the same number to open the door."
        ),
        answer=str(secret),
        hint="The number is even, a multiple of 3, and less than 35."
    )

    # Level 2: Pattern recognition
    lvl2 = Level(
        number=2,
        description=(
            "A screen shows a number sequence. A line of text below reads: "
            "\"Find the next number to calibrate the system.\""
        ),
        question="Sequence: 2, 4, 8, 16, ?\nWhat is the next number?",
        answer="32",
        hint="Each term is doubled from the previous one."
    )

    # Level 3: Word / counting logic
    lvl3 = Level(
        number=3,
        description=(
            "A console asks you to prove you are human by answering a "
            "simple observation question about a sentence."
        ),
        question=(
            "In the sentence \"Logic games sharpen problem solving skills\", "
            "how many words are there?"
        ),
        answer="6",
        hint="Count each separate word separated by spaces."
    )

    # Level 4: True/false reasoning
    lvl4 = Level(
        number=4,
        description=(
            "You reach a final terminal. A message appears: "
            "\"Only those who understand conditions may pass.\""
        ),
        question=(
            "Consider the rule: \"If a number is divisible by 4, then it is even.\"\n"
            "Is the number 12 a valid example that satisfies this rule? (yes/no)"
        ),
        answer="yes",
        hint="12 ÷ 4 is an integer, and 12 is even."
    )

    return [lvl1, lvl2, lvl3, lvl4]


def main():
    print(BANNER)
    print("WELCOME TO LOGIC LEVELS")
    print(BANNER)
    print("Solve a series of short logic-based puzzles.\n"
          "You have 3 attempts per level. Type your answer and press Enter.\n")

    levels = make_levels()
    for level in levels:
        success = level.play()
        if not success:
            print("Game over. You can restart the program to try again.")
            break
    else:
        print(BANNER)
        print("🎉 CONGRATULATIONS! You solved all logic levels.")
        print(BANNER)


if __name__ == "__main__":
    main()
