from flask import Flask, request
from flask_cors import CORS
from paraphraser import Paraphraser 
import json
import os

paraphraser = Paraphraser()
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def check_request_body():
    if request.data:
        body = dict(json.loads(request.data))
        text = body['text']
        
        print("Request body: ", body)
        print("Text: ", text)

        if request.get('translate') == "False":
            paraphrases = paraphraser.paraphraseia(text, translate=False)
            return paraphrases

        paraphrases = paraphraser.paraphraseia(text)
        return paraphrases
    else:
        return "Request body does not exist."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)