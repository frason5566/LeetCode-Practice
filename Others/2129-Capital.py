def C(title):
    title = title.lower()
    words = title.split(' ')
    # print(words)
    for i, word in enumerate(words):
        if len(word) > 2:
            word = word[0].upper() + word[1:]
            words[i] = word
            print(word)
    return ' '.join(words) 
    # pass


def main():
    print(C("capitaLize tHe SENtence"))

main()