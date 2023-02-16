import nltk
from nltk.collocations import BigramAssocMeasures, BigramCollocationFinder

# Load your corpus into a list of strings
corpus = ['this is sentence one', 'this is sentence two', 'this is sentence three']

# Tokenize the corpus into individual words
tokens = [nltk.word_tokenize(sent) for sent in corpus]

# Compute the frequency distribution of words in the corpus
freq_dist = nltk.FreqDist([word for sent in tokens for word in sent])

# Define the bigram association measure to use
bigram_measure = BigramAssocMeasures()

# Create a bigram collocation finder from the tokens
bigram_finder = BigramCollocationFinder.from_words([word for sent in tokens for word in sent])

# Apply the bigram association measure to the bigram collocation finder to compute the mutual information between words
bigram_finder.apply_freq_filter(5)  # Only consider bigrams that occur at least 5 times
bigram_scores = bigram_finder.score_ngrams(bigram_measure.pmi)

# Print the top 10 bigram scores (i.e. pairs of words with the highest mutual information)
for score in bigram_scores[:10]:
    print(score)
