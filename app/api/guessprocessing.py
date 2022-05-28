from app import app
from flask import jsonify, url_for, request
from app.api.errors import bad_request,error_response
import json


count=1
@app.route("/api/guessattempt",methods=['POST'])
def guessprocessing():
    a = request.get_json()
    data = request.json
    #this will be replaced with a call to the DB and getting the image's metadata
    response = {}
    if data['guess'] == data['correctanswer']:
        response['correct'] = "correct"
    else:
        #pixelate.pixel("bmo.png",5)

        response['correct'] = 'incorrect'
    return jsonify(response)


