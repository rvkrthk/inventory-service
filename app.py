from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api, Resource, fields
import utils

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
class Product(db.Model):
    id = db.Column('id', db.Integer,primary_key = True)
    name = db.Column(db.String(256))
    description = db.Column(db.String(1024))
    price = db.Column('price', db.Float)
    quantity = db.Column('quantity', db.Integer)

db.create_all()

api = Api(app, version='0.0.1', title='Inventory-Service microservice', 
    description='inventory microservice for learning'
)
ns = api.namespace('product', description="Products Namespace")
product_parser = utils.get_product_parser()
product_model = utils.get_product_model(api)

@ns.route("/api/v1/product")
@api.doc()
class Products(Resource):
    """
    This resource represents the Product
    """

    @ns.doc('list products')
    @ns.marshal_list_with(product_model)
    def get(self):
        return Product.query.all()

    @ns.doc(parser=product_parser)
    @ns.response(200, description="success", model=product_model)
    @ns.expect(product_model)
    @ns.marshal_with(product_model)
    def post(self):
        product_from_payload = product_parser.parse_args()
        product = Product(
            id = product_from_payload['id'],
            name = product_from_payload['name'],
            description = product_from_payload['description'],
            price = product_from_payload['price'],
            quantity = product_from_payload['quantity']
        )
        db.session.add(product)
        db.session.commit()
        return product


@app.route('/')
def hello_inventory():
    return "Hello From inventory Service!"

if __name__ == '__main__':
    app.run(port=8080, host="0.0.0.0")