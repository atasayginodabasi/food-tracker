from datetime import datetime, timedelta
from flask_wtf import FlaskForm
from wtforms import SubmitField, DateField
from wtforms.validators import DataRequired


class DateSelectionForm(FlaskForm):
    start_date = DateField("Start Date",
                           default=datetime.now().date() - timedelta(days=7),
                           validators=[DataRequired()])
    end_date = DateField("End Date",
                         default=datetime.now().date(),
                         validators=[DataRequired()])

    submit = SubmitField("Query")
