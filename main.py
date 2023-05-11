from flask import *
import memeSearcher

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        redirect("/")
    return render_template("home.html", meme=memeSearcher.pickMeme()) 

if __name__ == "__main__":
    app.run()
