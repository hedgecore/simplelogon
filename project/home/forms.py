from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired, Length, Email

class MessageForm(Form):
    name= TextField('Name', validators=[DataRequired()])
    email = TextField(
        'Email', validators=[DataRequired(), Email(message=None), Length(min=6, max=40)])

