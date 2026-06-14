# this is a Flask web application that displays personal information.

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return (
        "<p>Roshan Manjal is my name.</p>"
        "<p>My age is 20.</p>"
        "<p>My hobby is coding.</p>"
        "<p>I live in Ambernath.</p>"
    )


app.run()
