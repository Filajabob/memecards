import os


class Constants:
    with open("../assets/text/token.txt", 'r') as f:
        TOKEN = f.read()

    USERS_JSON = os.path.abspath("../assets/text/users.json")
