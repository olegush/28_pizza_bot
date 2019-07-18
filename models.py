from app import db


class Pizza(db.Model):
    __tablename__ = 'pizza'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.Text)
    choices = db.relationship('Choice')

    def __repr__(self):
        return "{'title': %r, 'description': %r, 'choices': %r}" % \
                (self.title, self.description, self.choices)


class Choice(db.Model):
    __tablename__ = 'choice'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    price = db.Column(db.Float)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'))

    def __repr__(self):
        return "{'title': %r, 'price': %r}" % (self.title, self.price)
