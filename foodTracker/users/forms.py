from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed
from foodTracker.models import User


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class RegistrationForm(FlaskForm):
    fullname = StringField("Name and Surname", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), EqualTo("pass_confirm",
                                                                             message="Passwords must match!")])
    pass_confirm = PasswordField("Verify Password", validators=[DataRequired()])
    submit = SubmitField("Create an Account!")

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("This username has been registered already!")
