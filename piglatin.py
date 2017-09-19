def piglatin():
    words = str(input("Ranslate-ay:")).split()
    for word in words:
            print(word[1:] + word[0] + "ay", end = " ")
    print()

piglatin()
