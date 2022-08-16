from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

@app.route('/')
def home():
    return "Today is Tuesday! **_**."


class User(Resource):
    def get(self):
        return jsonify({"msg": "Hello! I hope today is a good day."})

    def post(self):
        requested_data = request.get_json()
        name = requested_data['name']
        return jsonify({"msg": f"{name} don't give up, things will get better."})


api.add_resource(User, "/user")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

