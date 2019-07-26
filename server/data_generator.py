# This script will generate a sentence for every symptom in our 
# example sentences in a format which is acceptable for RASA NLU

import json

def generateSymptoms():   
        content = open('./symptoms.json', "r").read()
        j_content = json.loads(content)
        sents = ['- i have pain in [Name](symptom)','- i feel [Name](symptom)','- my [Name](symptom) hurt']
        res = []
        f = open("symptomsSentences.yml", "a")
        for j in sents:
                for i in j_content:
                # print(i['Name'])
                        temp = j
                        res.append(temp.replace('Name',i['Name'])+'\n')
        # print(res)
        for i in res:
                f.write(i)

        return

def generateDeseases():
        content = open('./deseases.json', "r").read()
        j_content = json.loads(content)
        sents = ['- i think I have [Name](desease)','- what is the symptoms of [Name](desease)?','- I got [Name](desease)', 'I want to know symptoms of [Name](desease)']
        res = []
        f = open("DeseasesSentences.yml", "a")
        for j in sents:
                for i in j_content:
                # print(i['Name'])
                        temp = j
                        res.append(temp.replace('Name',i['Name'])+'\n')
        # print(res)
        for i in res:
                f.write(i)
        return
        
generateDeseases()