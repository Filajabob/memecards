import classes
import json

options = ['c', 'd']

with open("../assets/text/users.json", 'r') as f:
    data = json.load(f)

me = classes.load_user(data["4"])
dummy = classes.load_user(data["3"])

battle = classes.Battle(me, dummy, me.cards, dummy.cards)


while True:
    for card in battle.cdeck:
        print(f"{card.name}\nLevel {card.level}")

    me_card = input("Select your card: ")

    for card in me.cards:
        if me_card == card.name:
            me_card = card
            break
    else:
        raise KeyError("Couldn't find requested card.")

    battle.rotate(0, 0, 'c', "primary")
