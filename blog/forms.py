# final_project/blog/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class EntryForm(FlaskForm):
    title = StringField('Tytuł wpisu', validators=[DataRequired()])
    body = TextAreaField('Treść wpisu', validators=[DataRequired()])
    is_published = BooleanField('Opublikowany')
    submit = SubmitField('Zapisz wpis')