# This is a test script to see how our bot answers our messages

from rasa_nlu.model import Interpreter
from rasa_core.agent import Agent
from rasa_core.utils import EndpointConfig
from rasa_core.interpreter import RasaNLUInterpreter

core_endpoint_config = EndpointConfig(url='http://localhost:5055/webhook')
interpreter = RasaNLUInterpreter('models/default/chat')
agent = Agent.load('models/dialogue', interpreter=interpreter, action_endpoint = core_endpoint_config)
print("Your bot is ready to talk! Type your messages here or send 'stop'")

while True:
    a = input()
    if a == 'stop':
        break
    responses = agent.handle_message(a)
    for response in responses:
        print('Bot:',response["text"])

