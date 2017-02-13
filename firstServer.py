import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

if __name__ == "__main__":
    pno = os.environ.get("PORT", 4567)
    port = int(pno)
    app.run(host='localhost', port=port)