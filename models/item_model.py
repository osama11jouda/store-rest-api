from db import db
class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision = 2))
    storeId = db.Column(db.Integer , db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')


    def __init__(self,name,price,storeId):
        self.name = name
        self.price = price
        self.storeId = storeId

    def json(self):
        return {'id':self.id,'name':self.name , 'price':self.price,'store id':self.storeId}

    def save_item_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_item_from_db(self):
        db.session.delete(self)
        db.session.commit()