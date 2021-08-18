from flask_restful import Resource ,reqparse
from functions.search import SearchFunctions
from models.user_model import UserModel

class RegisterUser(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',type = str , required = True , help = 'username is required')
    parser.add_argument('password',type = str , required = True , help = 'password is required')

    def post(self):
        try:
            data = RegisterUser.parser.parse_args()
            user = SearchFunctions.find_user_by_name(data['username'])
            if user:
                return{'message':'fail: user already exists'},404
            newUser = UserModel(**data)
            newUser.save_user_to_db()
            return{'message':'success : new user created'},201
        except:
            return{'message':'fail: server error'},500

