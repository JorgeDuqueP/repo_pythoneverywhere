from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Mira mi aplicación desde GitHub segunda parte</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"
if __name__ == '__mail__':
    app.run()
