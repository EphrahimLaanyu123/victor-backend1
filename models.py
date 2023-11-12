from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Properties(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    available = db.Column(db.Boolean, nullable=False, default=True)
    image = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
             "id": self.id,
            "name": self.name,
            "location": self.location,
            "bedrooms": self.bedrooms,
            "bathrooms": self.bathrooms,
            "price": self.price,
            "available": self.available,
            "image": self.image,
        }
