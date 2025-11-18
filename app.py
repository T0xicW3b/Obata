from flask import Flask

app = Flask(__name__)
app.secret_key = "abc"

from views import *

if __name__ == "__main__":
    app.run(debug=True) 