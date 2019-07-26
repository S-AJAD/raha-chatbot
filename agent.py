# This script will return similar symptoms and deseases to our data

import similarity

def agent(data):
    if data['entities'][0]['entity'] == 'desease':
        similar = similarity.similarityWithDeseases(data['entities'][0]['value'])


    if data['entities'][0]['entity'] == 'symptom' :
        similar = similarity.similarityWithSymptoms(data['entities'][0]['value'])

    # print(similar)
    return similar