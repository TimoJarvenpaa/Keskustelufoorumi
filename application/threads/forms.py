from flask_wtf import FlaskForm
from wtforms import StringField, validators

class ThreadForm(FlaskForm):
    title = StringField("Thread title", [validators.Length(min=2)])
 
    class Meta:
        csrf = False