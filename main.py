#Using Flask, also jsonify to create json response
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

#Creating Flask application
app = Flask(__name__)
api = Api(app) #Wrapping our APP in  API, which says wee are using REST API
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app) #wrapping app into a database

resource_fields = {
    'id': fields.Integer,
    'name' : fields.String,
    'views' :fields.Integer,
    'likes' :fields.Integer
}

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, primary_key=True)
    likes = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f"Video(name={name}, views = {views}, likes={likes})"

#Comment this after running the first time
#db.create_all() #Creates the database when we run the first time

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video is required", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video is required", required=True)

#videos = {}

'''
def abort_if_video_id_doesnt_exit(video_id):
    if video_id not in videos:
        abort(404, message="Couldn't find the video...")

def abort_if_video_exists(video_id):
    abort(409, message="Video with the same ID exists already")
'''

#Making a class with resource for different method
class video(Resource):
    def get(self, video_id):
        result = VideoModel.query.get(id=video_id)
        return
    
    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201
    
    def delete(self, video_id):
        abort_if_video_id_doesnt_exit(video_id)
        del videos[video_id]
        return '', 204


api.add_resource(video, "/video/<int:video_id>")


# To run server and Flask application, debug =True to specify this is a debug mode
if __name__ == "__main__":
    app.run(debug=True)
