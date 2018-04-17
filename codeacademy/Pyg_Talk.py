# PygTalk

pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print("Palavra original:\t", original)
    word = original
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
    print("Palavra em pyg:\t\t", new_word)

else:
    print("Formato inválido")
