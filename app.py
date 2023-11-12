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


class PropertiesList(Resource):
    def get(self):
        properties = Properties.query.all()
        return [property.serialize() for property in properties]
    
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
        return {'message': 'Property added successfully'}

api.add_resource(PropertiesList, '/properties')

if __name__ == '__main__':
    app.run(debug=True)