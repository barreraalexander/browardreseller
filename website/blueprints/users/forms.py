from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,\
                    SubmitField, BooleanField,\
                    SelectField, SelectMultipleField,\
                    RadioField, FloatField,\
                    MultipleFileField

from datetime import datetime

class LoginForm(FlaskForm):
    pass

class RegisterForm(FlaskForm):
    pass

class OrderForm(FlaskForm):
    cart_content = StringField('Cart Content')
    submit_order = SubmitField('submit')


class RemoveItemForm(FlaskForm):
    removing_id = StringField('To Remove')
    submit_remove = SubmitField('REMOVE')

class CheckoutForm(FlaskForm):
    shipping_to = StringField('Shipping To')
    payment_info = StringField ('Payment Info')
    submit_order = SubmitField('Checkout')
