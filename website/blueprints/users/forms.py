from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,\
                    SubmitField, BooleanField,\
                    SelectField, SelectMultipleField,\
                    RadioField, FloatField,\
                    MultipleFileField

from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField

from datetime import datetime

class LoginForm(FlaskForm):
    pass

class RegisterForm(FlaskForm):
    pass

class OrderForm(FlaskForm):
    cart_content = StringField('Cart Content')
    submit_order = SubmitField('CHECKOUT')


class RemoveItemForm(FlaskForm):
    removing_id = StringField('To Remove')
    submit_remove = SubmitField('REMOVE')

class CheckoutForm(FlaskForm):
    shipping_to = StringField('Shipping To')
    payment_info = StringField ('Payment Info')
    submit_order = SubmitField('Checkout')


        
class AddtoCart (FlaskForm):
    item_id = StringField ('Item ID')
    submit_atc = SubmitField ("Add To Cart")