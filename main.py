#Using Flask, also jsonify to create json response
from flask import Flask, request, jsonify

#Creating Flask application
app = Flask(__name__)

#Create a route to direct incoming API requests to backend resources
@app.route("/")
def home():
    return "Home"

# Get Request
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id" : user_id,
        "name" : "Jeevan Paudel",
        "email" : "jeevan@api.com",
        "age" : 55,
        "ishuman" : True
    }
    #query parmas
    query_params = request.args.get('query')
    if query_params:
        user_data["query"] = query_params
    
    return jsonify(user_data), 200

# Post Request
@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data), 201

# To run flask server
if __name__ == "__main__":
    app.run(debug=True)
