from flask_wtf import FlaskForm
from wtforms import TextAreaField, validators

class MessageForm(FlaskForm):
    content = TextAreaField("Message", [validators.Length(min=2, max=500)])
 
    class Meta:
        csrf = False