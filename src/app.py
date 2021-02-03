"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/member', methods=['POST'])
def handle_post(): 
    status = 200
    body = request.JSON
    try:
        # this is how you can use the Family datastructure by calling its methods
        member = jackson_family.add_member(body)
        if member == False:
            response_body ={
                "status" : "Member not found"
            }
        return jsonify(response_body), 200
    except:
        response_body = {
            "status" : "Not Ok"
        }
    status = 500
    return jsonify(response_body), status

@app.route('/members', methods=['GET'])
def handle_get_members(): 
    status = 200
    
    try:
        # this is how you can use the Family datastructure by calling its methods
        members = jackson_family.get_all_members()
        response_body = members

        return jsonify(response_body), 200

    except:
        response_body = {
            "status" : "Not Ok"
        }
    status = 500

    return jsonify(response_body), status

@app.route('/member/<int:member_id>', methods=['GET'])
def handle_get_specific_members(member_id): 
    status = 200
    body = request.JSON
    if body is None:
        response_body = {
        "status" : "Body is empty. Try again."
        }
        status = 500
    else:
        try:
            # this is how you can use the Family datastructure by calling its methods
            member = jackson_family.get_member(member_id)
            response_body = member
        
        except:
            response_body = {
                "status" : "Not Ok"
            }
            status = 500

    return jsonify(response_body), status


    # for i,x in enumerate(self._members):
    #     delete

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
