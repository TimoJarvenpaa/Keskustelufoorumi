from flask_wtf import FlaskForm
from wtforms import TextAreaField, validators

class MessageForm(FlaskForm):
    content = TextAreaField("Message", [validators.Length(min=2)])
 
    class Meta:
        csrf = False