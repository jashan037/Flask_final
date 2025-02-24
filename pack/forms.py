from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import Length, DataRequired, Email, EqualTo, ValidationError, NumberRange
from pack.models import Registerdb

class Register(FlaskForm):
    def validate_email(self,em):
        obj = Registerdb.query.filter_by(email=em.data).first()
        if obj:
            raise ValidationError('Email Already Registered')

    name = StringField(label='Your name', validators=[Length(min=3,max=30), DataRequired()])
    email = StringField(label='Email', validators=[Email(), DataRequired()])
    password = PasswordField(label='Password', validators=[Length(min=8), DataRequired()])
    password2 = PasswordField(label='Re-enter password', validators=[EqualTo('password'), DataRequired()])
    submit = SubmitField(label='Create your account')

class Login(FlaskForm):
    email = StringField(label='Email', validators=[Email(), DataRequired()])
    password = PasswordField(label='Password', validators=[Length(min=8)])
    submit = SubmitField(label='Sign in')

class RatingForm(FlaskForm):
    rating = IntegerField('Rating', validators=[
        DataRequired(),
        NumberRange(min=1, max=10, message="Rating must be between 1 and 10")
    ])
    review = TextAreaField('Review', validators=[
        DataRequired(),
        Length(min=10, max=500, message="Review must be between 10 and 500 characters")
    ])
    submit = SubmitField('Submit Rating')

class SearchForm(FlaskForm):
    search_query = StringField('Search', validators=[DataRequired()])
    submit = SubmitField('Search')
