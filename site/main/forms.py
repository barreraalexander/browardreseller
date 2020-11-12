from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField,\
                    SubmitField, BooleanField,\
                    SelectField, SelectMultipleField,\
                    RadioField, FloatField,\
                    MultipleFileField

from wtforms.validators import DataRequired, Length, Email,\
                                EqualTo, ValidationError

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
    #
    uploaded_to = SelectMultipleField ('Upload To')
    imgfiles = MultipleFileField ('Photos')
    submit_new_item = SubmitField ("Submit")
    submit_update_item = SubmitField ("Submit")

class UploadItemForm (FlaskForm):
    item = RadioField ('Item')
    upload_to = SelectMultipleField ('Upload To')
    submit_upload_item = SubmitField ("Submit")
    pass

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


class UploadRoloForm (FlaskForm):
    item_id = SelectField ('Item ID', choices=["Done"])
    submit_upload_item = SubmitField ("Submit")

        
