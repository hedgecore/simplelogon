from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired, Length, Email

class MessageForm(Form):
    title= TextField('Title', validators=[DataRequired()])
    description = TextField(
        'Description', validators=[DataRequired(), Email(message=None), Length(min=6, max=40)])

