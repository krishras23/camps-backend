import flask
from flask_cors import CORS
from flask import request, jsonify
import json

from dbhelper import create_child, delete_child, get_enrollments, \
    add_camp, delete_camp, update_camp_price, update_camp_ages, get_camps, update_child

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


@app.route('/', methods=["GET"])
def showing_enrollments():
    all_enrollments = get_enrollments()
    enrollments_dict = {}
    i = 1
    z = 0
    for x in all_enrollments:
        enrollments_dict[i] = all_enrollments[z]
        i = i + 1
        z = z + 1
    return jsonify(enrollments_dict)


@app.route('/add_kid', methods=["POST"])
def adding_kid():
    data = request.get_json()
    name = data["name"]
    allergies = data["allergies"]
    age = data["age"]
    create_child(name, allergies, age)
    return ""


@app.route('/update_kid_age', methods=["PATCH"])
def updating_kid():
    data = request.get_json()
    name = data["name"]
    new_age = data["new_age"]
    update_child(name, new_age)
    return ""


@app.route('/delete_kid', methods=["DELETE"])
def deleting_kid():
    data = request.get_json()
    name = data["name"]
    delete_child(name)
    return ""


## admin permissions

@app.route('/show_camps', methods=["GET"])
def showing_camps():
    all_camps = get_camps()
    camps_dict = {}
    i = 1
    z = 0
    for x in all_camps:
        camps_dict[i] = all_camps[z]
        i = i + 1
        z = z + 1
    json_string = json.dumps(camps_dict)
    return json_string


@app.route('/get_schedule', methods=["GET"])
def getting_schedule():
    data = request.get_json()
    print(data)




@app.route('/add_camp', methods=['POST'])
def adding_camp():
    print('Received add camp request')
    data = request.get_json()
    name = data['name']
    description = data['description']
    MIN_AGE = data['MIN_AGE']
    MAX_AGE = data['MAX_AGE']
    price_per_week = data['price_per_week']
    print('Adding a new camp')
    add_camp(name, description, MIN_AGE, MAX_AGE, price_per_week)
    return ""


@app.route('/delete_camp', methods=['DELETE'])
def deleting_camp():
    data = request.get_json()

    CampID = data['CampID']
    print(CampID)
    delete_camp(CampID)
    return ""


@app.route('/update_camp_price', methods=['PUT'])
def updating_camp_price():
    data = request.get_json()
    CampID = data['CampID']
    new_price = data['new_price']
    update_camp_price(CampID, new_price)
    return ""


@app.route('/update_camp_ages', methods=['PUT'])
def updating_camp_ages():
    data = request.get_json()
    new_MIN_AGE = data['new_MIN_AGE']
    new_MAX_AGE = data['new_MAX_AGE']
    CampID = data['CampID']
    update_camp_ages(CampID, new_MIN_AGE, new_MAX_AGE)
    return ""


app.run()
