def CreateVocabulary(filename):
    global word
    # use a set to store different words in 'word.txt' and create a vocabulary set
    vocabulary = set()

    try:
        word = open(filename, "r")  # read the word.txt

        for line in word.readlines():  # read it line by line
            line = line.strip()  # clean the space before or after the words
            vocabulary.add(line)  # add words of every line into vocabulary set
    except IOError:
        print("Errors in read vocabulary text")  # handle the error
    finally:
        word.close()  # close the reader to save memory

    return vocabulary  # get the vocabulary
