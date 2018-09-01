from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help='This field cannot be blank.')
    parser.add_argument('store_id', type=int, required=True, help='This field cannot be blank.')

    @jwt_required
    def get(self, name):
        try:
            item = ItemModel.find_by_name(name)
        except:
            return {'message': 'Database retrieval failed'}
        if item:
            return item.json(), 200
        else:
            return {'message': 'Item not found'}, 400

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': 'Item with name {} already exists'.format(name)}, 400
        data = Item.parser.parse_args()
        item = ItemModel(name, **data)
        try:
            item.save_to_db()
        except:
            return {'message': 'Insertion error occurred'}, 500
        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            ItemModel.delete_from_db()
        return {'message': '{} has been deleted'.format(name)}

    def put(self, name):

        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item:
            item.price = data['price']
        else:
            item = ItemModel(name, **data)
        item.save_to_db()

        return item.json()


class ItemList(Resource):
    def get(self):
        return {'items': [item.json for item in ItemModel.find_all()]}