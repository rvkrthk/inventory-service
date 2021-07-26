from flask import Flask,jsonify
import os
import logging
from flask_restplus import Api, Resource
from models import db, Product
import parsers

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
username = os.getenv('MYSQL_USERNAME', 'qtdevops')
password = os.getenv('MYSQL_PASSWORD', 'qtdevops')
server = os.getenv('MYSQL_SERVER', 'localhost')
database = os.getenv('MYSQL_DATABASE', 'inventoryservicedb')
DATABASE_URI = f"mysql+pymysql://{username}:{password}@{server}/{database}"
app.logger.debug(f"Database uri is {DATABASE_URI}")
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_ECHO'] = True
db.init_app(app)

api = Api(app, version='0.0.1', title='Inventory Service', description='Sample microservice for kubernetes')

ns = api.namespace('product', description='Product Namespace')
product_parser = parsers.get_product_parser()
product_model = parsers.get_product_model()

@ns.route('/initialize')
@api.doc()
class Initialize(Resource):

    @api.response(200, 'Success')
    @api.response(500, 'Error with Database Intitialziation')
    def get(self):
        try:
            db.create_all()
        except Exception as e:
            app.logger.error(f'Following Error Occurred {e}')
            return jsonify({"error": e}), 500

@ns.route('/product')
@api.doc()
class Product(Resource):

    @ns.doc('list products')
    @ns.marshal_list_with(product_model)
    def get(self):
        return Product.query.all()

    @ns.doc(parser=product_parser)
    @ns.response(200,description='success', model=product_model)
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
    return 'Hello from inventory'

if __name__ == '__main__':
    app.run(port=8080, debug=True, host="0.0.0.0")

