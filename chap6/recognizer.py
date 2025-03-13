"""
A grammer checker for sentences in a subset of English
defined by the following grammer rules:
sentence = nounphrase verbphrase
nounphrase = article noun
verbphrase = verb nounphrase prepositionalphrase
prepositionalphrase = preposition nounphrase

The parts of speech are nouns, verbs, articles,
and prepositions.
Inputs: purported sentences
Outputs: Ok, grammatically correct or
Not ok grammatically incorrect
"""
articles = ("A", "THE")

nouns = ("BOY", "GIRL", "BAT", "BALL")

verbs = ("HIT", "SAW", "LIKED")

prepostions = ("WITH", "BY")

def sentence(words):
    return nounPhrase(words) and verbPhrase(words)

def nounPhrase(words):
    if len(words) < 2:
        return False
    else:
        article = words.pop(0)
        noun = words.pop(0)
        return article in articles and noun in nouns
    main()
def verbPhrase(words):
    if len(words) == 0:
        return False
    else:
        verb = words.pop(0)
        return verb in verbs and nounPhrase(words) and prepositionalPhrase(words)

def prepositionalPhrase(words):
    if len(words) == 0:
        return False
    else:
        prepostion = words.pop(0)
        return prepostion in prepositions and nounPhrase(words)

def main():
    while True:
        userInput = input("Enter a sentence or press return to quit: ")
        if userInput == "":
            return
        else:
            words = userInput.upper().split()
            if sentence(words):
                print("Ok, grammatically correct!")
            else:
                print("not ok, grammatically incorrect")
if __name__ == "__main__":
    main()