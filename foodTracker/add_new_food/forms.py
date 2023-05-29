from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class NewFoodForm(FlaskForm):
    food_name = StringField("Name of the Food", validators=[DataRequired()])
    protein = IntegerField("Protein", validators=[DataRequired()])
    carbohydrates = IntegerField("Carbohydrates", validators=[DataRequired()])
    fat = IntegerField("Fat", validators=[DataRequired()])
    submit = SubmitField("Create the new Food")
