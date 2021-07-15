import flask
from flask import request, jsonify

from dbhelper import create_child, update_child, delete_child, get_enrollments

app = flask.Flask(__name__)
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
    student_id = data["student_id"]
    allergies = data["allergies"]
    age = data["age"]
    create_child(student_id, name, allergies, age)
    return ""


@app.route('/update_kid', methods=["POST"])
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


app.run()
