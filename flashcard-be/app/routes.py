import os
from . import create_app
from . import db
from .models import Category, Card
from flask import abort, jsonify, request

app = create_app(os.getenv("FLASK_CONFIG_ENV", "dev"))

@app.route("/categories", methods=["GET"])
def get_categories():
    categories = Category.query.all()
    return jsonify([category.to_json() for category in categories])


@app.route("/category/<int:id>", methods=["GET"])
def get_category(id):
    category = Category.query.get(id)

    if category is None:
        abort(404)
    
    return jsonify(category.to_json())


@app.route("/category", methods=["POST"])
def create_category():
    if not request.json:
        abort(400)
        
    category = Category(
        name = request.json.get("name")
    )
    db.session.add(category)
    db.session.commit()

    return jsonify(category.to_json()), 201


@app.route("/category/<int:id>", methods=["PUT"])
def update_category(id):
    if not request.json:
        abort(400)
        
    category = Category.query.get(id)

    if category is None:
        abort(404)

    category.name = request.json.get("name", category.name)

    db.session.commit()

    return jsonify(category.to_json())


@app.route("/category/<int:id>", methods=["DELETE"])
def delete_category(id):
    category = Category.query.get(id)

    if category is None:
        abort(404)
    
    db.session.delete(category)
    db.session.commit()

    return jsonify({
        "result": "Delete successfully"
    })


@app.route("/cards", methods=["GET"])
def get_cards():
    cards = Card.query.all()
    return jsonify([card.to_json() for card in cards])


@app.route("/card/<int:id>", methods=["GET"])
def get_card(id):
    card = Card.query.get(id)

    if card is None:
        abort(404)
    
    return jsonify(card.to_json())


@app.route("/card", methods=["POST"])
def create_card():
    if not request.json:
        abort(400)

    if Category.query.get(request.json.get("category_id")) is None:
        return jsonify({
            "result": "Category does not exist"
        }), 404
        
    card = Card(
        front = request.json.get("front"),
        back = request.json.get("back"),
        category_id = request.json.get("category_id")
    )
    db.session.add(card)
    db.session.commit()

    return jsonify(card.to_json()), 201


@app.route("/card/<int:id>", methods=["PUT"])
def update_card(id):
    if not request.json:
        abort(400)
        
    card = Card.query.get(id)

    if card is None:
        abort(404)

    if Category.query.get(request.json.get("category_id")) is None:
        return jsonify({
            "result": "Category does not exist"
        }), 404

    card.front = request.json.get("front", card.front)
    card.back = request.json.get("back", card.back)
    card.category_id = request.json.get("category_id", card.category_id)

    db.session.commit()

    return jsonify(card.to_json())


@app.route("/card/<int:id>", methods=["DELETE"])
def delete_card(id):
    card = Card.query.get(id)

    if card is None:
        abort(404)
    
    db.session.delete(card)
    db.session.commit()

    return jsonify({
        "result": "Delete successfully"
    })
