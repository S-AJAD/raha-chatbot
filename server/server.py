# This script is our server. Our mobile app will connect with this server

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
import urllib
import json
from io import BytesIO
from rasa_nlu.model import Interpreter
import agent
from rasa_core.agent import Agent
from rasa_core.utils import EndpointConfig
from rasa_core.interpreter import RasaNLUInterpreter
import re

core_endpoint_config = EndpointConfig(url='http://localhost:5055/webhook')
interpreter = RasaNLUInterpreter('models/default/chat')
agent = Agent.load('models/dialogue', interpreter=interpreter, action_endpoint = core_endpoint_config)

def getAnswer(text):
    responses = agent.handle_message(text)
    for response in responses:
        answer = response["text"]
        # print("answer:" + answer)
    return answer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)
        self.end_headers()
        query = urlparse(self.path).query
        query_components = dict(qc.split("=") for qc in query.split("&"))
        encodedStr = query_components['text']
        x = urllib.parse.unquote(encodedStr)
        print(x)
        clean = re.sub(r"[,.;@#?!&$]+\ *", " ", x)
        responses = agent.handle_message(clean)
        answer=""
        for response in responses:
            answer = response["text"]
            print(answer)
        json_string = json.dumps({'text': answer})
        t = bytes(json_string,'utf-8')
        self.wfile.write(t)

httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
print("start")

httpd.serve_forever()