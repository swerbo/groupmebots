
# A very simple Flask Hello World app for you to get started with...
import requests,re, json,
from flask import Flask, request

import UsefulStrings

app = Flask(__name__)

gmaps_key = UsefulStrings.gmaps_key

@app.route('/')
def hello_world():
    return 'Hello from Flask! sd;kjfhglkjsdhfgjklhsdflgkjhsdfg '

@app.route('/bot/', methods=['POST', 'GET'])
def hello():
    try:
        request_json=request.data
        r_json = json.loads(request_json.decode())
        summoner = r_json["name"]
        if re.search('@NYCBROS', r_json["text"].upper()):
            text = "NYC bros have been summoned by " + summoner
            requests.post("https://api.groupme.com/v3/bots/post", json = {"text":text, "bot_id" : UsefulStrings.NYCBOT_ID,"attachments":[{"type":"mentions", "loci":[[0,1],[1,1],[2,1],[3,len(text)-4]],"user_ids": UsefulStrings.NYC_BROS}]})
    except:
        pass
    #with open("groupmestuff.txt","wb") as fo:
    #    fo.write(r_json)

    return "nyc bros"


@app.route('/bostonbros/', methods = ['GET','POST'])
def bostonbros():
    try:
        request_json=request.data
        r_json = json.loads(request_json.decode())
        summoner = r_json["name"]
        if re.search('@BOSTONBROS', r_json["text"].upper()):
            text = "Boston Bros have been summoned by " + summoner
            requests.post("https://api.groupme.com/v3/bots/post", json = {"text":text, "bot_id" : UsefulStrings.BOSTONBOT_ID,"attachments":[{"type":"mentions", "loci":[[0,1],[2,len(text)-2]],"user_ids": UsefulStrings.BOSTON_BROS}]})
    except:
        pass
    return "boston bros"

@app.route('/mapsbot/', methods = ['GET','POST'])
def mapsbot():
    request_json=request.data
    r_json = json.loads(request_json.decode())
    if re.search('@MAPSBOT', r_json["text"].upper()):
        #get address
        #encode address
        formatted_address="225+Manhattan+Ave+Brooklyn,+NY"
        r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=" + formatted_address + "&key={0}".format(UsefulStrings.gmaps_key),)
        r_json = r.json()
        lat = str(r_json["results"][0]["geometry"]["location"]["lat"])
        lng = str(r_json["results"][0]["geometry"]["location"]["lng"])
        requests.post("https://api.groupme.com/v3/bots/post", json = {"text":lat, "bot_id" : UsefulStrings.MAPS_BOT_ID})
    return "maps bros"




if __name__ == "__main__":
    app.run(debug=True)