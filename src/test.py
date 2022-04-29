import classes
import json


with open("../assets/text/users.json", 'r') as f:
    data = json.load(f)

user = classes.load_user(data["813548110193754134"])
print(user.cards[0].primary_attack())