from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

class GSignForm(FlaskForm):
    # name/object = fieldtype(label,validators)
    fullname = StringField("Full name",validators=[
        DataRequired(message="Full name is mandate"),
        Regexp(r"^[A-Za-z ]{3,50}$", message="Invalid Full name")
    ])
    password = PasswordField("Password", validators=[
        DataRequired(message="Passowrd is Mandate"),
        Regexp(r"^(?=.*[@!#$&])(?=.+[0-9])[A-Za-z0-9!@#$&]{8,}$", message="Invalid Password")
    ])
    gender = RadioField("Gender",choices=[
        ("male","Male"),
        ("female","FeMale"),
        ("other","Others")
    ], validators=[
        DataRequired(message="Selecting gender is mandate")
    ])
    email = EmailField("email", validators=[
        DataRequired(message="Email is mandate"),
        Regexp(r"^[a-z0-9]{3,}@[a-z]{2,}\.[a-z]{2,}$",message="Invalid Email")
    ])
    contact = StringField("Contact Number",validators=[
        DataRequired(message="Contact is mandate"),
        Regexp(r"^[0-9]{10}$",message="Invalid contact")
    ])
    terms = BooleanField("Accept the terms of Google to signup", validators=[
        DataRequired(message="Accepting terms is mandate")
    ])
    submit = SubmitField("Singup")