import requests
import UsefulStrings
from flask import Flask, request
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base= declarative_base()

#Create SQLAlchemy engine. From their website, a typical database url is:: dialect+driver://username:password@host:port/database
# mysql-python
engine = create_engine('mysql+mysqldb://swerbo:'+UsefulStrings.sqlpassword+'@swerbo.mysql.pythonanywhere-services.com')

# If ABOVE DOESNT WORK TRY:
#MySQL-connector-python
#engine = create_engine('mysql+mysqlconnector://scott:tiger@localhost/foo')

class Bro(Base):
    __tablename__ = 'bros'

    id=Column(Integer, primary_key=True)
    name= Column(String)
    birthday=Column(String)
    groupme_id=Column(Integer)
    address=Column(String)

    def __repr__(self):
        return "<Bro(name'%s', birthday='%s', groupme_id='%d', address='%s')>" % (self.name, self.birthday, self.groupme_id, self.address)

app = Flask(__name__)


@app.route('/birthdaybot/', methods = ['GET','POST'])
def birthdaybot():
    text=""
    requests.post("https://api.groupme.com/v3/bots/post", json = {"text":"Happy Birthday to Beautiful BRONAME!", "bot_id" : UsefulStrings.MAPS_BOT_ID, "attachments":[{"type":"mentions", "loci":[[0,1],[2,len(text)-2]],"user_ids": UsefulStrings.BOSTON_BROS}]})
    return "Birthday Brah"




if __name__ == "__main__":
    app.run(debug=True)