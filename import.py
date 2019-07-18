import json
from app import db
from models import Pizza, Choice
from db.catalog import catalog

choice_id = 1
for pizza_id, pizza_data in enumerate(catalog, 1):
    pizza = Pizza(
                id=pizza_id,
                title=pizza_data['title'],
                description=pizza_data['description'])
    print(pizza_id, pizza)
    db.session.add(pizza)
    for choice_data in pizza_data['choices']:
        choice_id += 1
        choice = Choice(
                    id=choice_id,
                    title=choice_data['title'],
                    price=choice_data['price'],
                    pizza_id=pizza_id)
        print(choice_id, choice)
        db.session.add(choice)
db.session.commit()
