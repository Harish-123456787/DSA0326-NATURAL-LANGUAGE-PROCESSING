import nltk
from nltk.parse.earleychart import EarleyChartParser
from nltk.grammar import CFG

# Define the grammar
grammar = CFG.fromstring("""
    S  -> NP VP
    NP -> Det N
    VP -> V NP
    Det -> 'the'
    N  -> 'cat' | 'dog'
    V  -> 'chased' | 'saw'
""")

# Create the Earley chart parser
parser = EarleyChartParser(grammar)

# Sentence to be parsed
sentence = "the cat chased the dog".split()

# Parse the sentence and print parse trees
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
