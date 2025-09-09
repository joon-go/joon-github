from flask import Flask
from utils.helper import greet

app = Flask(__name__)

@app.route("/")
def hello():
    return greet("GitLab User")

if __name__ == "__main__":
    app.run(debug=True)