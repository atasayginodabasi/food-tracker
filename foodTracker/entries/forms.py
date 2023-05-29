from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, DateField
from wtforms.validators import DataRequired, InputRequired
from foodTracker.models import Foods


class NewEntryForm(FlaskForm):
    date = DateField("Date", validators=[DataRequired()])
    food_selection = SelectField(label='Select a Food that you had Today',
                                 choices=[],
                                 validators=[InputRequired()])

    def __init__(self):
        result = [x for x in Foods.query.with_entities(Foods.food_name, Foods.id).order_by(Foods.food_name.asc()).all()]

        super().__init__()
        self.food_selection.choices = [(x[1], x[0]) for x in result]

    submit = SubmitField("Register")
