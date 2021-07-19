"""SQLAlchemy models for blogly."""

import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

db = SQLAlchemy()


DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)


class User(db.Model):
    """Site user."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)

    posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")

    def __repr__(self):
       return f"<Name: {self.full_name}>"

    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"


class Post(db.Model):
    """Blog post."""

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
       return f"<Title: {self.title} | Content: {self.content} | Created At: {self.created_at} | User ID: {self.user_id}>"



class PostTag(db.Model):

   __tablename__ = "posts_tags"

   post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)
   tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)

   def __repr__(self):
      return f"<Post ID: {self.post_id} | Tag ID: {self.tag_id} >"



class Tag(db.Model):

   __tablename__ = "tags"

   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.Text, nullable=False, unique=True)

   posts = db.relationship('Post', secondary='posts_tags', backref='tags')

   def __repr__(self):
      return f"<Tag ID: {self.id} | Name: {self.name} >"










    

   