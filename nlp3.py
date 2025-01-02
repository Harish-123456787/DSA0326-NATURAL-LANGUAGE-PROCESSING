import nltk
from nltk.corpus import wordnet

# Ensure WordNet is downloaded
nltk.download('wordnet')

def explore_word_meanings(word):
    # Get synsets for the word
    synsets = wordnet.synsets(word)
    
    if not synsets:
        print(f"No meanings found for '{word}' in WordNet.")
        return
    
    # Iterate over all synsets and display their meanings and examples
    for synset in synsets:
        print(f"Meaning ({synset.pos()}): {synset.definition()}")
        
        examples = synset.examples()
        if examples:
            print(f"Example: {examples[0]}")  # Display the first example
        else:
            print("No example available.")
        print()

# Example usage
word_to_explore = "bank"
explore_word_meanings(word_to_explore)
