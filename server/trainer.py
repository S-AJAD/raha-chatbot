# This script will train our bot with our knowledge.

from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Interpreter
from rasa_core.policies.fallback import FallbackPolicy
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.agent import Agent

training_data = load_data('data/nlu/smalltalk')
trainer = Trainer(config.load("config/config.yml"))
trainer.train(training_data)
model_directory = trainer.persist('./models/',fixed_model_name = 'chat')  # Returns the directory the model is stored in

fallback = FallbackPolicy(fallback_action_name="action_default_fallback",core_threshold=0.1,nlu_threshold=0.1)

agent = Agent('domain1.yml', policies=[KerasPolicy(epochs=150), fallback])
training_data = agent.load_data('data/stories1.md')
agent.train(training_data)
agent.persist('models/dialogue')

print('bot is ready.')
