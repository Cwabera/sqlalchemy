from flask import Blueprint, jsonify
from models import db, User

user_bp = Blueprint("user_bp", __name__)


@user_bp.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200