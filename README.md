# raha-chatbot
Raha is a simple chatbot based on RASA NLU and RASA Core. Raha composed of two parts. one of them is it's server and the other one is a simple android app. The server is written by Python and android app is written by React-Native. Raha was my major project when I was studying bachelor of science in computer science at Ferdowsi University of Mashhad and I develop it in 2019.

# How to run

1. Install Python (I used Python 3.6.7)
2. Install all packages in pip-list.txt and conda-list.txt
3. cd to server folder
4. run the following command: python -m rasa_core_sdk.endpoint --actions actions
5. run the following command: python server.py
6. back and then cd to mobileBot folder
9. run your android emulator
7. tun the following command: react-native run-android

# What I have used

- gifted-chat for react-native
- Apimedic
- RASA Core and NLU
