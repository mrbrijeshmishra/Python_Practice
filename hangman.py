import random

word_list = ["aardvark", "baboon", "camel"]
def user_input():
    rand_word = random.choice(word_list)
    original_word = rand_word.lower()
    wrong_attempt = 0
    print(rand_word)
    word_length = len(rand_word)
    new_word = ["_"]*word_length
    print("Word:","".join(new_word))

    while wrong_attempt < 3 and  len(rand_word) > 0:

        c = input("Enter guess alphabet:").lower()
        if c in rand_word:
            index = original_word.find(c)
            new_word[index] = c
            rand_word = rand_word.replace(c,"",1)
        else:
            wrong_attempt +=1
            print(f"It looks like this is your {wrong_attempt} wrong attempt.")

    if len(rand_word) == 0:
        print("Word matched successfully")
        print("Word:","".join(new_word))
    else:
        print("Guess limit reached")
        print(f"word was {original_word}")


user_input()
