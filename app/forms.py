from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, Email
from flask_wtf.csrf import CSRFError




class ContactForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    subject = StringField('Subject', validators=[InputRequired()])
    message = StringField('Message', validators=[InputRequired()])