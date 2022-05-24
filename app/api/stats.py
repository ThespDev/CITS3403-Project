from app import app
from flask import jsonify, url_for, request
from app.api.errors import bad_request,error_response

@app.route('/api/stats',methods=['POST'])
def statistics():
    data = request.json

