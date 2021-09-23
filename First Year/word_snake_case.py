word = input('Please enter your word: ')
word_size = len(word)
i = 0
while i < word_size:
    if i == word_size-1:
        print(word[i])
    if word[i] != ' ' and i != word_size-1:
        print(word[i], end = '_')
    i += 1