from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

from application.categories.forms import MultiCheckboxField

class ThreadForm(FlaskForm):
    title = StringField("Thread title", [validators.Length(min=2, max=100)])
    content = TextAreaField("Message", [validators.Length(min=2,max=500)])
    categories = MultiCheckboxField("Categories", [validators.DataRequired(message="You must select at least one category")], choices=[], coerce=int)
 
    class Meta:
        csrf = False

class EditThreadForm(FlaskForm):
    title = StringField("Thread title", [validators.Length(min=2, max=100)])
    categories = MultiCheckboxField("Categories", [validators.DataRequired(message="You must select at least one category")], choices=[], coerce=int)
 
    class Meta:
        csrf = False