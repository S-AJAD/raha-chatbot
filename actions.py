# In this script, we will make appropriate answers for the times when user is talking about symptoms

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import hmac, hashlib
import base64
import json
import agent
import similarity

# Define variables
i=0
symptoms =[]
deseases = []
username = "e6HPc_GMAIL_COM_AUT"
password = "Zw23DqHy6a5Q4Rzj8"
authUrl = "https://authservice.priaid.ch/login"
healthUrl = "https://healthservice.priaid.ch"
language = "en-gb"

# Getting data from API
def loadFromWebService(token,action):

   extraArgs = "token=" + token + "&format=json&language=en-gb"
   if "?" not in action:
      action += "?" + extraArgs
   else:
      action += "&" + extraArgs

   url = healthUrl + "/" + action
   response = requests.get(url)

   try:
      response.raise_for_status()
   except requests.exceptions.HTTPError as e:
      print ("----------------------------------")
      print ("HTTPError: " + e.response.text )
      print ("----------------------------------")
      raise

   try:
      dataJson = response.json()
   except ValueError:
      raise requests.exceptions.RequestException(response=response)

   data = json.loads(response.text)
   return data       

#login API
def loginAPI():
   
   rawHashString = hmac.new(bytes(password, encoding='utf-8'), authUrl.encode('utf-8')).digest()
   computedHashString = base64.b64encode(rawHashString).decode()
   bearer_credentials = username + ':' + computedHashString
   postHeaders = {
            'Authorization': 'Bearer {}'.format(bearer_credentials)
   }
   responsePost = requests.post(authUrl, headers=postHeaders)
   data = json.loads(responsePost.text)
   return data["Token"]
   
#getting diagnosis from API
def loadDiagnosis(token,selectedSymptoms, gender, yearOfBirth):
   if not selectedSymptoms:
      raise ValueError("selectedSymptoms can not be empty")
   
   serializedSymptoms = json.dumps(selectedSymptoms)
   action = "diagnosis?symptoms={0}&gender={1}&year_of_birth={2}".format(serializedSymptoms, gender, yearOfBirth)
   return loadFromWebService(token,action)

#preparing answer for action_say
class ActionSay(Action):
   def name(self):
      return "action_say"

   def run(self, dispatcher, tracker, domain):
      # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict[Text, Any]]
      global i
      i = i + 1
      if len(tracker.latest_message['entities'])>0 :
         entity = tracker.latest_message['entities'][0]
         if(entity['entity'] =="symptom"):
            symptoms.append(entity['value'])
         if(entity['entity'] =="desease"):
            symptoms.append(entity['value'])
         if(len(symptoms) > 0):
            dispatcher.utter_message("OK. do you have any other symptoms? if it's done, tell me 'it's done'")
         else:
            dispatcher.utter_message("Sorry. I couldn't find anything. Please try again.")
         return
      else: 
         dispatcher.utter_message("Sorry. Something bad happened. please try again.")
      return
#preparing answer for action_say
class ActionDoneDesease(Action):
   def name(self):
      return "action_doneDesease"

   def run(self, dispatcher, tracker, domain):
      token1 = loginAPI()
      selectedSymptomsIds = []      
      similar = similarity.similarityWithSymptoms(symptoms[0])
      for symptom in symptoms:
         similar = similarity.similarityWithSymptoms(symptom)
         selectedSymptomsIds.append(similar[0]["ID"])
      r = loadDiagnosis(token1,selectedSymptomsIds, "Male", "1990")
      for issue in r:
         deseases.append(issue['Issue']['Name'])
      answer = "I think you may have one of these diseases:"
      for desease in deseases:
         answer +="\n" + desease
      dispatcher.utter_message(answer)
      symptoms.clear()
      deseases.clear()
      # print(symptoms)
      # print(deseases)

      return