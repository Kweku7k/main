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
    
    
    
class Forstaff(FlaskForm):
    surname= StringField('surname', validators=[DataRequired()])
    firstname = StringField('firstname', validators=[DataRequired()])
    maiden_name = StringField('maiden_name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    offical_email= StringField('offical_email', validators=[DataRequired()])
    personal_email = StringField('personal_email', validators=[DataRequired()])
    position = StringField('position', validators=[DataRequired()])
    department_directorate_unit = StringField('department_directorate_unit', validators=[DataRequired()])
    number = StringField('number', validators=[DataRequired()])
    gender = StringField('gender', validators=[DataRequired()])
    gender = StringField('gender', validators=[DataRequired()])
    rank = StringField('rank', validators=[DataRequired()])
    job_title = StringField('job_title', validators=[DataRequired()])
    employment_status = StringField('employment_status', validators=[DataRequired()])
    submit = SubmitField('Login')
    
    