import classes
import json


# dummy = classes.new_user("3")
# dummy.add_card(classes.Card(0, 100, 5))
#
# me = classes.new_user("4")
# me.add_card(classes.Card(0, 100, 5))

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

    battle.rotate(0, 0, 'c', "primary")
