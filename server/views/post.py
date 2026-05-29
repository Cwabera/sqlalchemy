from flask import Blueprint, request, jsonify
from models import db, Post

post_bp = Blueprint("post_bp", __name__)


@post_bp.route("/posts", methods=["GET"])
def get_posts():
    posts = Post.query.all()
    return jsonify([post.to_dict() for post in posts]), 200


@post_bp.route("/posts/<int:id>", methods=["GET"])
def get_post(id):
    post = Post.query.get(id)

    if not post:
        return jsonify({"error": "Post not found"}), 404

    return jsonify(post.to_dict()), 200


@post_bp.route("/posts", methods=["POST"])
def create_post():
    data = request.get_json()

    new_post = Post(
        title=data.get("title"),
        content=data.get("content"),
        user_id=data.get("user_id")
    )

    db.session.add(new_post)
    db.session.commit()

    return jsonify(new_post.to_dict()), 201


@post_bp.route("/posts/<int:id>", methods=["PATCH"])
def update_post(id):
    post = Post.query.get(id)

    if not post:
        return jsonify({"error": "Post not found"}), 404

    data = request.get_json()

    post.title = data.get("title", post.title)
    post.content = data.get("content", post.content)

    db.session.commit()

    return jsonify(post.to_dict()), 200


@post_bp.route("/posts/<int:id>", methods=["DELETE"])
def delete_post(id):
    post = Post.query.get(id)

    if not post:
        return jsonify({"error": "Post not found"}), 404

    db.session.delete(post)
    db.session.commit()

    return jsonify({"message": "Post deleted successfully"}), 200