from models.user_model import UserModel
from models.item_model import ItemModel
from models.store_model import StoreModel


class SearchFunctions:

    @classmethod
    def find_user_by_name(self,username):
        return UserModel.query.filter_by(username = username).first()

    @classmethod
    def find_user_by_id(self,_id):
        return UserModel.query.filter_by(id = _id).first()

    @classmethod
    def find_item_by_name(self,name):
        return ItemModel.query.filter_by(name = name).first()

    @classmethod
    def find_item_by_id(self,_id):
        return ItemModel.query.filter_by(id = _id).first()

    @classmethod
    def find_store_by_name(self,name):
        return StoreModel.query.filter_by(name = name).first()

    @classmethod
    def find_store_by_id(self,_id):
        return StoreModel.query.filter_by(id = _id).first()

    @classmethod
    def find_item_in_store(self,name,storeId):
        return ItemModel.query.filter_by(name = name , storeId = storeId).first()        