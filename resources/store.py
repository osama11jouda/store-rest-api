from flask_restful import Resource ,reqparse
from functions.search import SearchFunctions
from models.item_model import ItemModel
from models.store_model import StoreModel

class Store(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('new_name',type = str , help = 'new namw is required')


    def get(self,name):
        try:            
            store = SearchFunctions.find_store_by_name(name)
            if store:
                return StoreModel.json(store),201
            return{'message':'fail: store not found'},404
        except:
            return{'message':'fail: server error'},500

    def post(self,name):
        try:        
            store = SearchFunctions.find_store_by_name(name)
            if store:
                return {'message':'fail : this store is already exists'},404        
            
            newStore = StoreModel(name)
            StoreModel.save_store_to_db(newStore)
            return {'message': 'seccess : store created'},201
        except:
            return{'message':'fail: server error'},500

    def delete(self,name):
        try:        
            store = SearchFunctions.find_store_by_name(name)
            if store:
                StoreModel.delete_store_from_db(store)                    

            return {'message': 'seccess : store deleted'},200
        except:
            return{'message':'fail: server error'},500 

    def put(self,name):
        try:     
            data = Store.parser.parse_args()   
            store = SearchFunctions.find_store_by_name(name)
            if store:
                store.name = data['new_name']
                StoreModel.save_store_to_db(store)
                return {'message':'succes : name changed'},200                 

            return {'message': 'fail : store not found'},400
        except:
            return{'message':'fail: server error'},500                       

class StoresList(Resource):
    def get(self):         
        try:
            return {'stores':[StoreModel.json(store) for store in StoreModel.query.all()]}
        except:
            return {'message':'an error happened'}