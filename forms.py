from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField, SelectField, IntegerField,PasswordField, SearchField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

class Forlecturer(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    name = StringField('Email', validators=[DataRequired()])
    school = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    image = PasswordField('Password', validators=[DataRequired()])
    telephone = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    
    