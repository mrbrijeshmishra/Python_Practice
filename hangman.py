import random

word_list = ["aardvark", "baboon", "camel"]
def user_input():
    original_word = random.choice(word_list).lower()
    remaining_letters = list(original_word)
    new_word = ["_"] * len(original_word)
    wrong_attempt = 0

    print(original_word)
    print("Word:","".join(new_word))

    while wrong_attempt < 3 and remaining_letters:

        c = input("Enter guess alphabet:").lower()
        if c in remaining_letters:
            index = original_word.find(c)
            new_word[index] = c
            remaining_letters.remove(c)
            print(new_word)
        else:
            wrong_attempt +=1
            print(f"It looks like this is your {wrong_attempt} wrong attempt.")

    if not remaining_letters:
        print("Word matched successfully")
        print("Word:","".join(new_word))
    else:
        print("Guess limit reached")
        print(f"word was {original_word}")


user_input()
