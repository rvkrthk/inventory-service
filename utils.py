from flask_restx import reqparse, fields, Api


def get_product_parser():
    """
    This method returns the product parser
    :return:
    """
    product_parser = reqparse.RequestParser()
    product_parser.add_argument('id', type=int)
    product_parser.add_argument('name')
    product_parser.add_argument('description')
    product_parser.add_argument('price', type=float)
    product_parser.add_argument('quantity', type=int)
    return product_parser


def get_product_model(api: Api):
    """

    :type api: Api
    """
    product_model = api.model('ProductModel', {
        'id': fields.Integer,
        'name': fields.String,
        'description': fields.String,
        'price': fields.Float,
        'quantity': fields.Integer
    })
    return product_model
