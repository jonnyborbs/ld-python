import ldclient
from ldclient.config import Config

from flask import Flask, jsonify
import requests

app = Flask(__name__)

user = {
    "key": "aa0ceb1234",
    "firstName": "Mara",
    "lastName": "Jade",
    "email": "mjade@coruscant.gov",
    "custom": {
      "groups": ["Jedi"]
    }
}

@app.route("/")
def get_feature():  
    ldclient.set_config(Config("sdk-ba6a8b5e-78ad-4950-923d-fe6356640835"))
    trek_or_wars = ldclient.get().variation("trekOrWars", user, "No Data")
    if trek_or_wars == "wars":
        r = requests.get("https://swapi.dev/api/people/1/").json()
        ldclient.get().close()
        return jsonify(r)
    elif trek_or_wars =="trek":
        r = requests.post('http://stapi.co/api/v1/rest/character/search?name=Jean-Luc&gender=M').json()
        ldclient.get().close()
        return jsonify(r)
    else:
        text = "Choose your players. Choose their path. Double their peril. Double your winnings."
        return text
    
if __name__ == '__main__':
    app.run(debug=True)