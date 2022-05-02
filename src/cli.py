import classes
import json

options = ['c', 'd']

# me = classes.new_user("1")
# me.add_card(classes.cards.PythonCard(0, 0, 5, "Dick"))
#
# dummy = classes.new_user("2")
# dummy.add_card(classes.cards.SpiderCard(0, 0, 5, "8 Dicks"))

with open("../assets/text/users.json", 'r') as f:
    data = json.load(f)

me = classes.load_user(data["1"])
dummy = classes.load_user(data["2"])


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

    print(battle.rotate(0, 0, 'c', "primary", "primary"))
