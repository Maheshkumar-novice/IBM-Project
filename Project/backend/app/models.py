from app import db

class Retailer(db.Model):
    __tablename__ = 'retailers'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(140), unique=True, nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)
    retailer_id = db.Column(db.Integer, db.ForeignKey('retailers.id'), nullable=False)

  