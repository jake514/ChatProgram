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
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)


# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

#------------------------------------------------------------app.routes
@app.route("/", methods=["POST", "GET"])
def index():
    channels = db.execute("SELECT * FROM channels").fetchall()
    newChannel = ""
    if newChannel != "" and newChannel != None:
        db.execute("INSERT INTO channels(name) VALUES (:name)", {"name":newChannel})
        channels = db.execute("SELECT * FROM channels").fetchall()
    return render_template('index.html', channels=channels)
    
    


@socketio.on("channelName")
def create(channelName):
    name = channelName["channelName"]
    print(name)
    if name != "" and name != None:
        print("entered if statement")
        nameExists= db.execute("SELECT name from channels WHERE name=:name", {"name":name}).fetchone()
        print(nameExists)
        if nameExists == None:
            print("new channel name")
            db.execute("INSERT INTO channels (name) VALUES (:name)", {"name":name})
            db.commit()
            print("added to database")
    emit("newChannel", {"channelName":channelName}, broadcast=True)


if __name__ == '__main__':
    socketio.run(app)