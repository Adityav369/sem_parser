import nltk


def tokenizeAndFilter(sentence):
    """
    tokenize the sentence
    """
    # TODO: make a custom tokenizer so can tokenize imp domain related chunks
    tokenized = nltk.word_tokenize(sentence)
    omitWords = {"The", "there are", "there is", "draw", "make", "construct",
                 "Construct", "Make", "Draw", "is", "an"}
    return [w for w in tokenized if not w in omitWords]


def seqLabel(tokenizedSent):
    func_type = {"Function"}
    set_type = {"Set"}
    # just have names as set name defines function
    set_relations = {"Intersection": "BinRelSet"}
    func_relations = {"Injection": "BinRelFunc",
                      "Bijection": "BinRelFunc", "Surjection": "BinRelFunc", "Bijection": "BinRelFunc"}
    directional = {"From", "To"}
    label = []
    for i, word in enumerate(tokenizedSent):
        capitalizedWord = word.capitalize()
        if capitalizedWord in func_type:
            label.append((capitalizedWord, "entityType"))
        elif capitalizedWord in set_type:
            label.append((capitalizedWord, "entityType"))
        elif capitalizedWord in func_relations.keys():
            label.append(
                (capitalizedWord, func_relations[capitalizedWord]))
        elif capitalizedWord in set_relations.keys():
            label.append(
                (capitalizedWord, set_relations[capitalizedWord]))
        elif capitalizedWord in directional:
            label.append((word, capitalizedWord))
        elif len(word) <= 2:
            label.append((word, "name"))
    return label
