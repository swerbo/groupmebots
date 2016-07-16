import requests
import UsefulStrings
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
#Connect to the brobook
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://swerbo:'+UsefulStrings.sqlpassword+'@swerbo.mysql.pythonanywhere-services.com/swerbo$brobook'
#db is an instance of SQLAlchemy
db = SQLAlchemy(app)

#turns the table bros into a python class
class bros(db.Model):


    id=db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String)
    birthday=db.Column(db.String)
    groupme_id=db.Column(db.Integer)
    address=db.Column(db.String)

    #toStringMethod
    def __repr__(self):
        return "<Bro(name='%s', birthday='%s', groupme_id='%d', address='%s')>" % (self.name, self.birthday, self.groupme_id, self.address)
    #Constructor
    def __init__(self, name, birthday, groupme_id, address):
        self.name=name
        self.birthday=birthday
        self.groupme_id=groupme_id
        self.address=address

#puts all bros into a list of bros
allbros=bros.query.all()
#Creates a list of the birthday bros
birthdaybros=[bros for bros in allbros if (bros.birthday.day == datetime.datetime.now().day and bros.birthday.month == datetime.datetime.now().month)]

@app.route('/birthdaybot/', methods = ['GET','POST'])
def birthdaybot():
    for i in range(0,len(birthdaybros)):
        requests.post("https://api.groupme.com/v3/bots/post", json = {"text":"Happy Birthday to Beautiful "+birthdaybros[i].name+"!", "bot_id" : UsefulStrings.MAPS_BOT_ID}) #I have to figure out mentions
        #requests.post("https://api.groupme.com/v3/bots/post", json = {"text":"Happy Birthday to Beautiful "+birthdaybros[i].name+"!", "bot_id" : UsefulStrings.MAPS_BOT_ID, "attachments":[{"type":"mentions", "loci":[[0,1]],"user_ids": +birthdaybros[i].groupme_id}]})
    return "Birthday Brah"


birthdaybot()

