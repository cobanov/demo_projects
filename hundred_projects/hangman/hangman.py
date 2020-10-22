# HANGMAN

lives = 10
answer = "cobanov"

solution = list("_" * len(answer))

while True:
    try:
        guess = input("guess a letter: ")[0]
    except:
        guess = "_"

    for index, letter in enumerate(answer):
        if letter in guess:
            if letter not in solution[index]:
                solution[index] = letter

    if guess not in answer:
        lives -= 1

    if "".join(solution) == answer:
        print("Won!")
        break

    if lives == False:
        print("Game Over!")
        break

    print(lives)
    print(solution)
