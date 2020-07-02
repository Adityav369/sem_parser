import nltk


def tokenizeAndFilter(sentence):
    """
    tokenize the sentence
    """
    # TODO: make a custom tokenizer so can tokenize imp domain related chunks
    tokenized = nltk.word_tokenize(sentence)
    for i, token in enumerate(tokenized):
        if token[-1] == '.' or token[-1]==" ":
            tokenized[i] = token[:len(token)-1]
        if token == "vector" or token == "Vector":
            if tokenized[i+1]=="space" or tokenized[i+1]=="Space":
                tokenized[i] = "Vector Space"
    omitWords = {"The", "there are", "there is", "draw", "make", "construct",
                 "Construct", "Make", "Draw", "is", "an", "Given", "given", ",", " ", ""}
    return [w for w in tokenized if not w in omitWords]


def seqLabel(tokenizedSent):
    types = {"Function", "Set", "Vector Space", "Vector"}
    # just have names as set name defines function
    relations = {"Injection": "BinRelFunc",
                      "Bijection": "BinRelFunc", "Surjection": "BinRelFunc", "Orthogonal": "BinRelVec", "Intersection": "BinRelSet", "+": "BinRelVec", "=": "BinRelVec"}
    directional = {"From", "To", "In"}
    named = set()
    label = []
    for i, word in enumerate(tokenizedSent):
        capitalizedWord = word.capitalize()
        if capitalizedWord in types or word in types:
            # print(capitalizedWord)
            label.append((capitalizedWord, "entityType"))
        elif capitalizedWord in relations.keys():
            label.append((capitalizedWord, relations[capitalizedWord]))
        elif capitalizedWord in directional:
            label.append((word, capitalizedWord))
        elif len(word) <= 2:
            if word not in named:
                label.append((word,"name"))
                named.add(word)
            else:
                label.append((word, "declaredBefore"))
    return label
