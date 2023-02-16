import math

# Define your corpus as a list of documents, where each document is a list of words
corpus = [
    ['this', 'is', 'document', 'one'],
    ['this', 'is', 'document', 'two'],
    ['this', 'is', 'document', 'three'],
]

# Compute the term frequency (TF) for each term in each document
tf = []
for doc in corpus:
    doc_tf = {}
    for term in doc:
        doc_tf[term] = doc_tf.get(term, 0) + 1
    tf.append(doc_tf)

# Compute the inverse document frequency (IDF) for each term in the corpus
idf = {}
N = len(corpus)
for doc in corpus:
    for term in set(doc):
        idf[term] = idf.get(term, 0) + 1
for term in idf:
    idf[term] = math.log(N / idf[term])

# Compute the TF-IDF for each term in each document
tfidf = []
for doc in tf:
    doc_tfidf = {}
    for term in doc:
        doc_tfidf[term] = doc[term] * idf[term]
    tfidf.append(doc_tfidf)

# Print the TF-IDF scores for each document
for i, doc_tfidf in enumerate(tfidf):
    print("Document", i+1)
    for term, score in doc_tfidf.items():
        print(term, ":", score)
    print()
