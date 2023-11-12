from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, request
from models import db, Properties

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///victor.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

migrate = Migrate(app, db)
api = Api(app)

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS, PUT, DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

class PropertiesList(Resource):
    def get(self):
        properties = Properties.query.all()
        return [property.to_dict() for property in properties]

    def post(self):
        property_data = request.get_json()
        new_property = Properties(
            name=property_data['name'],
            location=property_data['location'],
            bedrooms=property_data['bedrooms'],
            bathrooms=property_data['bathrooms'],
            price=property_data['price'],
            available=property_data['available'],
            image=property_data['image'],
        )
        db.session.add(new_property)
        db.session.commit()

        # Return the details of the newly added property
        return new_property.to_dict(), 201  # 201 status code indicates successful creation

api.add_resource(PropertiesList, '/properties')

if __name__ == '__main__':
    app.run(debug=True)
