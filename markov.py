import random as rand

#Takes the name of a text file with passages to be used for chain
#Returns dictionary of corresponding following words
def create_word_dict(textfile_name):
    worddict = {}
    passage = open(textfile_name)
    words = reduce(lambda x, y: x + y, 
                [line.split() for line in passage.readlines()])

    for i in xrange(len(words) - 1):
        if words[i] in worddict:
            worddict[words[i]].append(words[i+1])
        else:
            worddict[words[i]] = [words[i+1]]

    return worddict

#Takes in dictionary of words and those that follow
#Returns markov-chain generator
def nextword(dict_of_words, passage_length = 100):
    word = rand.choice(dict_of_words.keys())
    for i in xrange(passage_length):
        new_word = rand.choice(dict_of_words[word])
        yield new_word
        word = new_word

d = create_word_dict("sherlock.txt")
print " ".join(list(nextword(d)))
