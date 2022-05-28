from app import app
from flask import jsonify, url_for, request
from app.api.errors import bad_request,error_response

@app.route("/api/correctanswer",methods=['GET'])
def correctanswer():
    response = {}
    #Make a call to the DB to find today's correct answer
    answer = 'bmo'
    response['answer'] = answer
    return response
    

