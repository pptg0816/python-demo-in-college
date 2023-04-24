import CreateVocabulary
import SpellChecker

vocabulary = CreateVocabulary.CreateVocabulary("words.txt")
SpellChecker.SpellChecker(vocabulary, "original.txt")
SpellChecker.SpellChecker(vocabulary, "peter-pan.txt")
