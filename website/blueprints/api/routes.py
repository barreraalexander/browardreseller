from website import db, bcrypt
from website.models.coupon_code import CouponCode
from website.models.discount_item import DiscountItem
from website.models.user import User
from website.models.order import Order
from flask import url_for, redirect, request, Blueprint, flash
from flask_login import current_user
import json


api = Blueprint ('api', __name__)


@api.route('/get_coupons')
def get_coupons():
    models = CouponCode.get(getall=True)
    models_as_dict = [ model.as_dict for model in models ]
    return json.dumps(models_as_dict)

@api.route('/get_discounts')
def get_discounts():
    models = DiscountItem.get(getall=True)
    models_as_dict = [ model.as_dict for model in models ]
    return json.dumps(models_as_dict)



@api.route('/add_to_cart', methods=['GET', 'POST'])
def add_to_cart():
    if request.method == 'POST':
        if current_user.is_authenticated:
            user = current_user
        else:
            curr_ip = request.remote_addr
            user = User.get (by='ip_address', value=curr_ip)
        
        model_id = request.json


        cart_ls = user.cart.split('$')
        if model_id not in cart_ls:
            user.cart += (f"{model_id}$")
            User.update(user)
        else:
            return
    return



@api.route('/checkout_order', methods=['GET', 'POST'])
def checkout_order():
    if request.method == 'POST':
        if current_user.is_authenticated:
            user = current_user
        else:
            curr_ip = request.remote_addr
            user = User.get (by='ip_address', value=curr_ip)
        
        print ('FORM', request.form.get('shipping_to_zip'))
        mdict = {
            'user_id' : user._id,
            'card_csv' : request.form.get('card_csv'),
            'card_exp' : request.form.get('card_exp'),
            'card_number' : request.form.get('card_number'),
            'order_data' : user.cart,
            'shipping_to' : request.form.get('shipping_to'),
            'shipping_to_country' : request.form.get('shipping_to_country'),
            'shipping_to_state' : request.form.get('shipping_to_state'),
            'shipping_to_zip' : request.form.get('shipping_to_zip'),
            'is_fulfilled' : 0,
        }
        try:
            new_order = Order(mdict)
            Order.add(new_order)
            user.cart = ""
            user.update(user)
            flash ('we got your order')
            return redirect( url_for('users.order_summary', model_id=new_order._id) )
        except Exception as e:
            flash ('we were unable to complete your order')

    return redirect( url_for('users.index') )





# @api.route('/remove_item')
# def remove_item():
#     pass