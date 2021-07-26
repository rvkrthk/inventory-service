from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    """
    This represents an individual item in the inventory
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=256), nullable=False)
    description = db.Column(db.String(length=256), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return "<Product id={self.id} name={self.name}>"
