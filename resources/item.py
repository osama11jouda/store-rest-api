from flask_restful import Resource ,reqparse
from functions.search import SearchFunctions
from models.item_model import ItemModel

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',type = float , help = 'price is required')
    parser.add_argument('storeId',type = int , help = 'store id is required')
    

    def get(self,name):
        try:            
            item = SearchFunctions.find_item_by_name(name)
            if item:
                return item.json(),201
            return{'message':'fail: item not found'},404
        except:
            return{'message':'fail: server error'},500

    def post(self,name):
        data = Item.parser.parse_args()
        item = SearchFunctions.find_item_in_store(name, data['storeId'])
        if item:
            return {'message':'fail : this item is already exists'},404
        store = SearchFunctions.find_store_by_id(data['storeId'])
        if store:
            newItem = ItemModel(name, **data)
            newItem.save_item_to_db()
            return {'message': 'seccess : item created'},201
        return {'message': 'fail : store not found'},404

    def delete(self,name):
        data = Item.parser.parse_args()
        try:        
            item = SearchFunctions.find_item_in_store(name, data['storeId'])
            if item:
                ItemModel.delete_item_from_db(item)                    

            return {'message': 'seccess : item deleted'},200
        except:
            return{'message':'fail: server error'},500 

    def put(self,name):
        try:     
            data = Item.parser.parse_args()   
            item = SearchFunctions.find_item_by_name(name)
            if item:
                item.price = data['price']
                ItemModel.save_item_to_db(item)
                return {'message':'succes : item updated'},200   
            item = ItemModel(name, **data) 
            ItemModel.save_item_to_db(item)    
            return {'message': 'success : new item added'},201
        except:
            return{'message':'fail: server error'},500                       

class ItemsList(Resource):
    def get(self):
        try:
            return {'items':[ItemModel.json(item) for item in ItemModel.query.all()]}
        except:
            return {'message':'an error happened'}