from flask_wtf import FlaskForm
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField,\
                    SubmitField, BooleanField,\
                    SelectField, SelectMultipleField,\
                    RadioField, FloatField, \
                    IntegerField, MultipleFileField
from wtforms.fields.html5 import DateField

# class NewItemForm (FlaskForm):
#     category =  SelectField ('Categories')
#     c_type = StringField ('Item Type')
#     brand = StringField ('Brand')
#     model_num = StringField ('Model')
#     name = StringField ('Name')
#     colors = SelectMultipleField ('Colors')
#     size = StringField ('Size')
#     obj_condition = RadioField ('Condition')
#     #item pricing
#     orig_value = FloatField ('Original Value')
#     purchase_price = FloatField ('Purchase Price')
#     selling_price = FloatField ('Selling Price')
#     shipping_price = FloatField ('Shipping Price')
#     #
#     uploaded_to = SelectMultipleField ('Upload To')
#     imgfiles = MultipleFileField ('Photos')
#     submit_new_item = SubmitField ("Submit")
#     submit_update_item = SubmitField ("Submit")

# try adding a model, if a model is added, then return an edit form
class NewItemForm (FlaskForm):
    category =  SelectField ('Categories')
    c_type = StringField ('Item Type')
    brand = StringField ('Brand')
    model_num = StringField ('Model')
    name = StringField ('Name')
    colors = SelectMultipleField ('Colors')
    size = StringField ('Size')
    obj_condition = RadioField ('Condition')
    #item pricing
    orig_value = FloatField ('Original Value')
    purchase_price = FloatField ('Purchase Price')
    selling_price = FloatField ('Selling Price')
    shipping_price = FloatField ('Shipping Price')
    stock = IntegerField ('Stock')
    #
    uploaded_to = SelectMultipleField ('Upload To')
    imgfiles = MultipleFileField ('Photos')
    submit_new_item = SubmitField ("Submit")
    submit_update_item = SubmitField ("Submit")

class NewSaleForm (FlaskForm):
    item_id = StringField ('Item ID', render_kw={'readonly': True})
    purchase_price = FloatField ('Purchase Price', render_kw={'readonly': True})
    selling_price = FloatField ('Selling_Price')
    shipping_price = FloatField ('Shipping Price')
    uploaded_to = StringField ('Uploaded To')
    site_sold = RadioField ('Site Sold')
    submit_new_sale = SubmitField ("Submit")

class UpdateSaleForm (FlaskForm):
    pass

class UpdateItemForm (FlaskForm):
    pass


class RegisterForm(FlaskForm):
    register_email = StringField ('Email')
    register_password = StringField('Password')
    f_name = StringField ('First Name')
    l_name = StringField ('Last Name')
    submit_register = SubmitField('Register')

class LoginForm(FlaskForm):
    login_email = StringField ('Email')
    login_password = StringField('Password')
    submit_login = SubmitField('Login')


class FulfillForm(FlaskForm):
    fulfill_order_id = StringField ('order_id')
    submit_fulfill = SubmitField('Fulfill Order')


class AddItem(FlaskForm):
    pass

class EditItem(FlaskForm):
    pass

class SetGoalForm(FlaskForm):
    goal = IntegerField('Goal')
    submit_goal = SubmitField('Set Goal')


class NewCouponForm(FlaskForm):
    coupon_code = StringField('Coupon Code',
                                    render_kw={
                                        'size': 60,
                                        'placeholder': 'Only letters, numbers are allowed (no characters or spaces).'
                                        })
    discount_rate = IntegerField ('Discount Rate (in percent)',
                                    render_kw={
                                        'size': 2,
                                        'placeholder': '10%'
                                        })
    start_date = DateField('Start Date')
    expire_date = DateField('Expire Date')
    submit_new_coupon = SubmitField ('Submit')

class NewDiscountForm(FlaskForm):
    discount_item_id = StringField('Discount Item ID',
                                    render_kw={
                                        'size': 30,
                                        'placeholder': 'select an item below'
                                        })
    discount_rate = IntegerField ('Discount Rate (in percent)',
                                    render_kw={
                                        'size': 2,
                                        'placeholder': '10%'
                                        })
    start_date = DateField('Start Date')
    expire_date = DateField('Expire Date')
    submit_new_discount = SubmitField ('Submit')
    

