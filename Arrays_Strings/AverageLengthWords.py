def AverageLenWords(sentence):
    words = sentence.split()
    l = 0
    for word in words:
        l += len(word)
    return round((l / len(words)), 3) if len(words) > 0 else 0


print(AverageLenWords("adgrhy b cddefgh"))
