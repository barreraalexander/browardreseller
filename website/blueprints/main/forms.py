from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField
        
class AddtoCart (FlaskForm):
    item_id = StringField ('Item ID')
    submit_atc = SubmitField ("Add To Cart")