from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    hashed_password = db.Column(db.String(255))
    blogs = db.relationship('Blog', backref='author', lazy='dynamic')

    def encrypt_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def confirm_password(self, password):
        return check_password_hash(self.hashed_password, password)

    def __repr__(self):
        return f"<User: {self.username}>"


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    subtitle= db.Column(db.String(100))
    body = db.Column(db.Text)
    time_created = db.Column(db.DateTime, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"<Blog: {self.title}>"


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
