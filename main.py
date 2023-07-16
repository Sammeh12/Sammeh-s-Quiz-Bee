print("-------------------------")
print("Welcome to Sammeh's Quiz Bee!")

def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1
    
    for key in questions:
        print("-------------------------")
        for i in options[question_num-1]:
            print(i)
        guess = input("Answer: ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

def display_score(correct_guesses, guesses):

    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions)*100))
    print("Your score is: "+str(score)+"%")

def play_again():

    print("-------------------------")
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
    
questions = {
    "It is the ease with which programs can be read or understand.: ": "A",
    "What year was Common LISP developed?: ": "C",
    "Which of these are not a part of the Characteristics that Affect Reliability?: ": "B",
    "Is it true that Programming is easy?: ": "D"
}

options = [["A. Readability", "B. Writability", "C. Reliability", "D. Special Words"],
           ["A. 1960s", "B. 1970s", "C. 1980s", "D. 1990s"],
           ["A. Type Checking", "B. Data Types", "C. Aliasing", "D. Exception Handling"],
           ["A. Negative", "B. Never", "C. Nope", "D. All of the Above"]]

new_game()

while play_again():
    new_game()

print("Thank you for playing!")
