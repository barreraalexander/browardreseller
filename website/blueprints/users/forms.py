from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,\
                    SubmitField, BooleanField,\
                    SelectField, SelectMultipleField,\
                    RadioField, FloatField,\
                    MultipleFileField, DateField

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
    shipping_to = StringField('Address')
    shipping_to_country = SelectField('Country')
    shipping_to_state = SelectField('State/Province')
    shipping_to_zip = StringField('Zipcode', render_kw={
                                    'size': 5,
                                    'placeholder': 33324,
                                    }
                                )
    
    card_number = StringField ('Card Number')
    card_csv = StringField ('Security Code')
    card_exp = DateField ('Expiration Date')
    payment_info = StringField ('Payment Info')
    coupon_code = StringField ('Coupon Code')
    submit_order = SubmitField('Checkout')


        
class AddtoCart (FlaskForm):
    item_id = StringField ('Item ID')
    submit_atc = SubmitField ("Add To Cart")
