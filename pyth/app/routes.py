

from flask_restx import Namespace, Resource, fields, reqparse
from .services import get_coins, get_categories, get_coin_details
from .auth import api_key_required 

ns = Namespace('crypto', description='Crypto related operations')

# Pagination 
pagination_parser = reqparse.RequestParser()
pagination_parser.add_argument('page_num', type=int, default=1, help='Page number')
pagination_parser.add_argument('per_page', type=int, default=10, help='Items per page')

coin_model = ns.model('Coin', {
    'id': fields.String,
    'symbol': fields.String,
    'name': fields.String
})

category_model = ns.model('Category', {
    'category_id': fields.String,
    'name': fields.String
})

@ns.route('/coins')
class CoinList(Resource):
    @api_key_required  
    @ns.expect(pagination_parser)
    @ns.marshal_list_with(coin_model)
    def get(self):
        args = pagination_parser.parse_args()
        page_num = args['page_num']
        per_page = args['per_page']
        return get_coins(page_num, per_page)

@ns.route('/categories')
class CategoryList(Resource):
    @api_key_required 
    @ns.expect(pagination_parser)
    @ns.marshal_list_with(category_model)
    def get(self):
        args = pagination_parser.parse_args()
        page_num = args['page_num']
        per_page = args['per_page']
        return get_categories(page_num, per_page)

@ns.route('/coins/<string:coin_id>')
class CoinDetail(Resource):
    @api_key_required  
    @ns.marshal_with(coin_model)
    def get(self, coin_id):
        return get_coin_details(coin_id)