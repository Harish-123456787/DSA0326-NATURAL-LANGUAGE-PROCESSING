import math

# Given data
terms = ["chicken", "fried", "oil", "pepper"]
term_frequencies = [5, 4, 6, 7]
document_frequencies = [10, 2, 4, 5]
N = 10  # Total number of documents 

# Calculate TF-IDF for each term
tf_idf_scores = {}

for term, tf, df in zip(terms, term_frequencies, document_frequencies):
    # Prevent division by zero
    if df == 0:
        idf = 0
    else:
        idf = math.log(N / df)
    
    tf_idf = tf * idf
    tf_idf_scores[term] = tf_idf

# Print the TF-IDF scores
for term, score in tf_idf_scores.items():
    print(f"TF-IDF score for term '{term}': {score:.4f}")
