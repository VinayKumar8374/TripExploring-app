from flask import Flask, render_template
from data.destinations import destinations


app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "index.html",
        destinations=destinations
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
