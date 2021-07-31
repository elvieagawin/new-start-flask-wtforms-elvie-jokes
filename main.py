from flask import *
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
import requests
from joke_class import Joke
import json

# EXCEEDS API QUOTA
# url = "https://dad-jokes.p.rapidapi.com/random/joke?count=10"
#
# headers = {
#     'x-rapidapi-key': "609b2ed0c4msh32545e29c993771p14295ejsn49def6017fd8",
#     'x-rapidapi-host': "dad-jokes.p.rapidapi.com"
#     }
#
# response = requests.request("GET", url, headers=headers)
# data = response.json()
# print(data)
#
# for joke in data:
#     jokes_data = []
#     joke_obg = Joke(joke['_id'], joke['type'], joke['setup'], joke['punchline'])
#     jokes_data.append(joke_obg)
#     #print(jokes_data)

jokes_data = []
with open("dad_jokes.json", mode="r") as jokes_file:
    data = json.load(jokes_file)['body']
    for joke in data:
        joke_obg = Joke(joke['_id'], joke['type'], joke['setup'], joke['punchline'])
        jokes_data.append(joke_obg)
        print(len(jokes_data))
        #print(jokes_data)


app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def index():
    return render_template("index.html", all_jokes=jokes_data)

@app.route("/joke/<index>")
def view_joke(index):
    requested_post = None
    for joke_post in jokes_data:
        if joke_post.id == index:
            requested_post = joke_post
    return render_template("post.html", post=requested_post)


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    # Run the app in debug mode
    app.run(debug=True)