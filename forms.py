from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Email, Optional, URL, NumberRange, Length
# from wtforms.widgets.html5 import URLField

class AddPetForm(FlaskForm):
    name = StringField("Dog Name",  validators=[InputRequired(message="Dog Name can't be blank")])   
    # species = StringField("Species",  validators=[InputRequired(message="Species can't be blank")])
    species = SelectField("Species",  choices=[('cat', 'Cat'), ('dog', 'Dog'), ('por', 'Porcupine')])
    photo_url = StringField("Image URL", validators = [Optional(), URL()])
    age = IntegerField("Dogs Age", validators = [Optional(), NumberRange(min=0, max=30)])  
    notes = TextAreaField("Notes",  validators=[Optional()])
    available = BooleanField("Is available?")                          


class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField("Image URL", validators=[Optional(), URL()])

    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],
    )
    available = BooleanField("Is available?")
