from werkzeug.security import safe_str_cmp
from resources.user import UserModel

# The below create sets of dictionaries based on the content of the users list, with the key being the username and
# id respectively and the value for each being the entire user object associated with that name/id
# username_mapping = {user.username: user for user in users}
#
# userid_mapping = {user.id: user for user in users}


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    uid = payload['identity']
    return UserModel.find_by_id(uid)
