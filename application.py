# ----------------project 2 requirements-------------------------------------------------------------------------------------------------------------
# display name: user prompt to enter display name. Needs to be remembered
# channel creation: user can create new channel, cannot conflict with existing channel
# messages view: can see & store up to 100 most recent message (upon opening a channel)
# sending messages: text messages to other through channel. Contains display name & timestamp, all users on channel can see. Do not require reload
# remember channel: remembers which channel user was previously on (if window closes)
# personal touch: additional feature of my choosing
#----------------------------------------------------------------------------------------------------------------------------------------------------
import os

from flask import Flask, session, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
# socketio = SocketIO(app)

#------------------------------------------------------------app.routes
@app.route("/", methods=["POST", "GET"])
def index():
    return render_template('index.html')

    #MDN local storage