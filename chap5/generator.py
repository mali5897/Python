"""
Generates and displays sentences using simple grammer
and vocabulary. Words are chosen at random.
"""
import random

# Vocabulary: words in 4 different parts of speech

articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL")
verbs = ("HIT", "SAW", "LIKED")
preposition = ("WITH", "BY")


def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()
def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)
def verbPhrase():
    """Builds and returns verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()
def prepositionalPhrase():
    """Builds and returns the prepositional phrase."""
    return random.choice(preposition) + " " + nounPhrase()
def main():
    """Allow the user to input the number of sentences to generate."""
    number = int(input("Please enter the number of sentences: "))
    for count in range(number):
        print(sentence())

# The entry point for program execution
if __name__ == "__main__":
    main() 