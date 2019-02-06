from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class ThreadForm(FlaskForm):
    title = StringField("Thread title", [validators.Length(min=2, max=255)])
    content = TextAreaField("Message", [validators.Length(min=2,max=500)])
 
    class Meta:
        csrf = False