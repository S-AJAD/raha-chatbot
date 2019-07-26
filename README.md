# raha-chatbot
Raha is a simple chatbot based on RASA NLU and RASA Core. Raha composed of two parts. Raha acts like a virtual doctor. However, it is a friend when you need a friend. The server is written by Python. Raha was my major project when I was studying bachelor of science in computer science at Ferdowsi University of Mashhad and I develop it in 2019.

# How to run

1. Install Python (I used Python 3.6.7)
2. Install all packages in pip-list.txt and conda-list.txt
3. cd to server folder
4. edit action.py file and add your Apimedic's username and password
5. run the following command: python -m rasa_core_sdk.endpoint --actions actions
6. run the following command: python server.py
7. test the server using Postman with the following URL: localhost:1000/?test=you_message
8. Also, you can run test.py and have a conversation with Raha

# What I have used

- Apimedic
- RASA Core and NLU
