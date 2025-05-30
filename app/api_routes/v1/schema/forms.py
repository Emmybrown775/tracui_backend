from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, EmailField
from wtforms.validators import DataRequired, Email, ValidationError
import enum



class AccountType(enum.Enum):
    SUPPLIER = "SUPPLIER"
    RETAILER = "RETAILER"
    CONSUMER = "CONSUMER"

def enum_validator(enum_class):
    def _validate(form, field):
        if field.data not in [e.value for e in enum_class]:
            raise ValidationError(f'Invalid value: {field.data}. Allowed values are: {[e.value for e in enum_class]}')

    return _validate

class SignUpForm (FlaskForm):
    access_token = StringField("First Name", validators=[DataRequired()])
    access_secret = StringField("Last Name", validators=[])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    account_type = StringField("Gender", validators=[DataRequired(), enum_validator(AccountType)])
    private_key = StringField("PrivateKey", validators=[DataRequired()])
    address = StringField("Last Name", validators=[DataRequired()])
