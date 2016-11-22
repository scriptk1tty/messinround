import random

def get_random_word():
    words = ["adventure time, sleep, desktop, nausicaa, valley, wind, neopets"]
    word = words[random.randint(0, len(words))-1]
    return word

def show_word(word):
    for character in word:
        print(character, " ", end="")
    print("")

def get_guess():
    print("Enter a letter: ")
    return input()

def process_letter(letter, secret_word):
    result = False

    for i in range(0, len(secret_word)):
        if secret_word[i] == letter:
            result= True
    
    return result

def play_word_game():
    
    strikes = 0
    max_strikes = 3
    playing = True
    
    word = get_random_word()
    blanked_word = "_" * len(word)

    while playing:
        show_word(blanked_word)
        letter = get_guess()
        found = process_letter(letter, word)
        
        strikes += 1

        if strikes >= max_strikes:
            playing = False

            
    if strikes >= max_strikes:
        print("Loser!")
    else:
        print("Congratulations, you've won!")
              

print("READY PLAYER ONE")
play_word_game()
print("GAME OVER")