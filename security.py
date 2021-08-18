from functions.search import SearchFunctions
from models.user_model import UserModel


def authenticate(username,password):
    user = SearchFunctions.find_user_by_name(username)
    if user and user.password == password:
        return user


def identity(payload):
    user_id = payload['identity']
    return SearchFunctions.find_user_by_id(user_id)