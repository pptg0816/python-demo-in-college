global file, words


def SpellChecker(vocabulary, filename):
    global file, words
    try:
        file = open(filename, "r")
        words = []
        for line in file.readlines():
            line = line.strip()
            words.append(line.split(" "))  # read the txt that needs to be checked, split words by ' '
            # if necessary, import re , use re.split(r'[,;!?/t]', line) to handle various split.
    except IOError:
        print("Errors in read files that need to be checked")
    finally:
        file.close()

    checked = ""  # use string 'checked' to store text after checked
    for line in words:
        for word in line:
            if word not in vocabulary and word.lower() not in vocabulary:
                word = "[[" + word + "]]"  # if a word in text is not in vocabulary, add [[]] around this word
            checked = checked + word + " "
        checked = checked + "\n"

    try:
        new_filename = filename + "_checked.txt"
        file = open(new_filename, "w")  # create newfile to write in 'checked' string
        file.write(checked)
    except IOError:
        print("Errors in write checked files")
    finally:
        file.close()
