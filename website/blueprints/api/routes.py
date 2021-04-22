from website import db, bcrypt
from website.models.coupon_code import CouponCode
from website.models.discount_item import DiscountItem
from website.models.user import User
from flask import url_for, redirect, request, Blueprint
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

        user.cart += (f"{model_id}$")
        User.update(user)

        print (model_id)
        return
    #     cart_ls = user.cart.split('$')
    #     if recipe_id not in cart_ls:
    #         user.cart += (f"{recipe_id}$")
    #         User.update(user)
    #     else:
    #         return
    # return





# @api.route('/remove_item')
# def remove_item():
#     pass