import os
from flask import Flask
from flask_restful import Api ,Resource
from flask_jwt import JWT
from db import db
from security import authenticate,identity
from resources.register_user import RegisterUser
from resources.item import Item ,ItemsList
from resources.store import Store ,StoresList


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://jkmocrjuoigsny:09aeec041fc4a2554b0a57afa6bfaff7d1b338c826f0a3b1b341a88241b9c270@ec2-54-220-53-223.eu-west-1.compute.amazonaws.com:5432/dege5uu67in11g"


app.secret_key = "jose"
api = Api(app)

jwt = JWT(app,authenticate,identity)



api.add_resource(RegisterUser,'/register')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoresList,'/stores')
api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemsList,'/items')

if __name__ == '__main__':    
    app.run(port=5000,debug=True)