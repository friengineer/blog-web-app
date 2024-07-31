from app import db

# table for comments
comments = db.Table('comments',
        db.Column('post', db.Integer, db.ForeignKey('post.id')),
        db.Column('account', db.Integer, db.ForeignKey('account.id')))

# model for accounts in the database
class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String(500))
    comments = db.relationship('Post', secondary=comments, backref=db.backref('comments'), lazy='dynamic')

# model for blog posts in the database
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    date = db.Column(db.Date)
