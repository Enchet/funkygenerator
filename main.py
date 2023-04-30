from flask import *
import memeSearcher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", meme=memeSearcher.pickMeme()) 

if __name__ == "__main__":
    app.run()
