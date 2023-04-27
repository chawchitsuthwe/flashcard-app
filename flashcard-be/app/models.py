from . import db

class Category(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name
        }


class Card(db.Model):
    __table_name__ = "card"

    id = db.Column(db.Integer, primary_key=True)
    front = db.Column(db.Text, nullable=True)
    back = db.Column(db.Text, nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    category = db.relationship(Category, backref="category")

    def to_json(self):
        return {
            "id": self.id,
            "front": self.front,
            "back": self.back,
            "category": self.category.to_json()
        }
