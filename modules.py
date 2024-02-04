import re
from sklearn.feature_extraction.text import TfidfVectorizer

# tfidf_vectorizer = TfidfVectorizer()

import nltk
from nltk.corpus import stopwords

import nltk
from nltk.stem import WordNetLemmatizer


def remove_stopwords(val):
    words = val.split()
    filtered_words = [word for word in words if word.lower() not in stopwords.words('english')]
    return ' '.join(filtered_words)
def rem_punc(val):
    pattern = r'[^a-zA-Z0-9 ]'
    cleaned_text = re.sub(pattern, '', val)
    return cleaned_text

def lemmatize_text(val):
    lemmatizer = WordNetLemmatizer()
    words = nltk.word_tokenize(val)
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(lemmatized_words)