# This script will calculate similarity

import json
import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer

stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))


def cosine_sim(text1, text2):
        tfidf = vectorizer.fit_transform([text1, text2])
        return ((tfidf * tfidf.T).A)[0,1]


vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')


def similarityWithSymptoms(text):
    content = open('./symptoms.json', "r").read()
    j_content = json.loads(content)
    similar_symptoms = []
    for i in j_content:
        cosine = cosine_sim(text, i['Name'])
        if (cosine>0):
            data = i
            data['similarity'] = cosine
            similar_symptoms.append(data)
    return similar_symptoms


def similarityWithDeseases(text):
    content = open('./deseases.json', "r").read()
    j_content = json.loads(content)
    similar_deseases = []
    for i in j_content:
        cosine = cosine_sim(text, i['Name'])
        if (cosine>0):
            data = i
            data['similarity'] = cosine
            similar_deseases.append(data)
    return similar_deseases
