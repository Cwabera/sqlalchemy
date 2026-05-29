from app import app
from models import db, User, Post

with app.app_context():
    Post.query.delete()
    User.query.delete()

    user1 = User(
        username="charles",
        email="charles@example.com",
        password="password123"
    )

    db.session.add(user1)
    db.session.commit()

    post1 = Post(
        title="First Post",
        content="This is my first post.",
        user_id=user1.id
    )

    post2 = Post(
        title="Second Post",
        content="This is another post.",
        user_id=user1.id
    )

    db.session.add_all([post1, post2])
    db.session.commit()

    print("Database seeded successfully.")