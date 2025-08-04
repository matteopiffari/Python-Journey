# From a starting phrase returns:
#   - How many unique words are in the phrase
#   - How many times each word appears in the phrase
#   - The longest word in the phrase
#   - The unrepeated words in the phrase

def uniqueWords(phrase):
    words = phrase.split()
    wordsSet = set(({}))

    for word in words:
        wordsSet.add(word)
    
    return len(wordsSet)


def wordTimeCounter(phrase):
    words = phrase.split()
    wordsDict = {}

    for word in words:
        if(word in wordsDict):
            wordsDict[word] += 1
        else:
            wordsDict[word] = 1
    
    return wordsDict


def longestWord(phrase):
    words = phrase.split()
    lWord = words[0]

    for word in words:
        if len(word) > len(lWord):
            lWord = word
    
    return lWord


def unrepeatedWords(phrase):
    wordsDict = wordTimeCounter(phrase)
    wordsList = []

    for key, value in wordsDict.items():
        if(value == 1):
            wordsList.append(key)

    return wordsList


def main():
    phrase = "The quick brown fox jumps over the lazy dog. The dog was not amused by the fox."
    phrase = phrase.replace(".", "")
    phrase = phrase.lower()

    print(uniqueWords(phrase))
    print(wordTimeCounter(phrase))
    print(longestWord(phrase))
    print(unrepeatedWords(phrase))

if __name__ == "__main__":
    main()