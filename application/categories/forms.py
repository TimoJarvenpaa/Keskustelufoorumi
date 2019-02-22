from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, SelectField, validators, widgets

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class AddCategoryForm(FlaskForm):
    name = StringField("Category", [validators.Length(min=2, max=20)])
 
    class Meta:
        csrf = False

class SelectCategoryForm(FlaskForm):
    category = SelectField("Choose a category", [validators.DataRequired()], choices=[])
 
    class Meta:
        csrf = False