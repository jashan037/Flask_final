from pack import app,db,bcrypt
from datetime import datetime

class Registerdb(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(length=30),nullable=False)
    email=db.Column(db.String(length=100),nullable=False)
    password=db.Column(db.String(length=90),nullable=False)
    # Define the relationship without conflicting backref
    ratings = db.relationship('Rating', backref='author', lazy=True)

    @property
    def passhash(self):
        return self.passhash
    
    @passhash.setter
    def passhash(self,pas):
        self.password=bcrypt.generate_password_hash(pas).decode('utf-8')

    def checkpass(self,pas):
        return bcrypt.check_password_hash(self.password,pas)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    image_url = db.Column(db.String(500), nullable=False)
    ratings = db.relationship('Rating', backref='movie', lazy=True)

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    review = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('registerdb.id'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
