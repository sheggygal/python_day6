REverseinp= input("Enter a sentence: ").lower()

words = REverseinp.split()

reversed_words = list(reversed(words))

reversed_words[0] = reversed_words[0].capitalize()

reversed_sentence = ' '.join(reversed_words)

print(reversed_sentence)
