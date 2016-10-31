import csv
from sklearn.feature_extraction.text import TfidfVectorizer


docs = []
with open('authors_info.csv') as f:
    reader = csv.reader(f, delimiter='|')
    next(reader)  # skip headers
    for row in reader:
        docs.append(row[1])

vect = TfidfVectorizer(min_df=1, max_df=0.8)

tfidf = vect.fit_transform(docs)
res = (tfidf * tfidf.T).toarray()
