from website import bcrypt, db
from website.blueprints.users.forms import AddtoCart,OrderForm, RemoveItemForm, CheckoutForm
from website.components.ItemDiv import component as item_div_cmpnt
from website.components.ItemFlexy import component as item_flexy_cmpnt
from website.models.coupon_code import CouponCode
from website.models.item import Item
from website.models.order import Order
from website.models.sale import Sale
from website.models.user import User
from flask import render_template, url_for,\
                  redirect, request, Blueprint,flash

from flask_login import current_user
from datetime import datetime, timedelta
from website.blueprints.users import STATES, COUNTRIES
import json


users = Blueprint ('users', __name__)

@users.route ("/", methods=["GET", "POST"])
def index ():
    form = AddtoCart()
    models = Item.get(getall=True)
    
    flexs = [ item_flexy_cmpnt(model) \
            for model in models ]

    promo_item = Item.get(by="_id", value="fa9f2a892e7239c9a6086539d776")
    slider_item = Item.get(by="_id", value="fe6cf011aae691791ea17c9834f8")

    slider_item.reduction = 30
    slider_item.reduced_price = slider_item.selling_price - (round(slider_item.selling_price * slider_item.reduction/100, 2))


    slider_item.sale_start = datetime(year=2021, month=3, day=6)
    slider_item.sale_end = datetime(year=2021, month=4, day=10)
    slider_item.sale_daysleft = str(slider_item.sale_end - datetime.now()).split(',')[0].split(' ')[0]

    if request.method == "POST":
        if form.validate_on_submit and form.submit_atc.data:
            model_id = f"{form.item_id.data}$"
            ip_requesting = request.remote_addr
            user = User.get(by='ip_address', value=ip_requesting)

            if user:
                pass
            else:
                user = User.get_temp_user(ip_requesting)
                User.add(user)
    
            user.cart += model_id
            User.update(user)
            return redirect( url_for('users.index') )

    # print ('REQUEST', request)
    return render_template('users/_index.html',
                            flexs=flexs,
                            form=form,
                            models=models,
                            promo_item=promo_item,
                            slider_item=slider_item)

@users.route("/test_me", methods=["GET", "POST"])
def test_me ():
    pass

@users.route ("/inventory/<string:model_id>", methods=["GET", "POST"])
def inv_item (model_id):
    model = Item.get(by="_id", value=model_id)
    form = AddtoCart()

    if request.method == "POST":
        if form.validate_on_submit and form.submit_atc.data:
            model_id = f"{form.item_id.data}$"
            ip_requesting = request.remote_addr
            user = User.get(by='ip_address', value=ip_requesting)

            if user:
                pass
            else:
                user = User.get_temp_user(ip_requesting)
                User.add(user)
    
            user.cart += model_id
            User.update(user)
            return redirect( url_for('users.index') )

    return render_template('users/_inv_item.html', model=model, form=form)

    
@users.route ('/cart', methods=['GET', 'POST'])
def cart ():
    curr_ip = request.remote_addr
    user = User.get(by='ip_address', value=curr_ip)

    if user:
        item_ids = user.cart_as_ls()
        models = [ Item.get(by='_id', value=item_id) \
                   for item_id in item_ids ]
    else:
        models = ['none yet']

    order_form = OrderForm ()
    remove_form = RemoveItemForm()
    if request.method == 'POST':
        if order_form.validate_on_submit and order_form.submit_order.data:
            return redirect(url_for('users.checkout', model_id=user._id))

        elif remove_form.validate_on_submit and remove_form.submit_remove.data:
            remove_id = remove_form.removing_id.data
            cart = user.cart_as_ls()            
            cart.remove(remove_id)
            user.cart = "$".join(cart) + '$'
            User.update(user)
            return redirect(url_for('users.cart'))

    for model in models:
        if model==None:
            models.remove(model)


    cart_total = 0
    for item in models:
        cart_total += item.selling_price

    cart_summary = {
        "item_count" : len(models),
        "cart_total" : round(cart_total, 2)
    }

    return render_template('users/_cart.html', title='Cart',
                            models=models,
                            cart=user.cart,
                            order_form=order_form,
                            remove_form=remove_form,
                            cart_summary=cart_summary,
                            user=user)

@users.route('/checkout/<string:model_id>', methods=['GET', 'POST'])
def checkout (model_id):
    user = User.get(by='_id', value=model_id)
    item_ids = user.cart_as_ls()
    coupon_codes = CouponCode.get(getall=True)


    inv_models = [ Item.get(by='_id', value=item_id) \
                   for item_id in item_ids ]

    retail_total = 0
    shipping_total = 0
    item_count = len(inv_models)

    for model in inv_models:
        retail_total += model.selling_price
        shipping_total += model.shipping_price

    order_summary = {
        'shipping_total' : round(retail_total, 2),
        'retail_total' : round(shipping_total/item_count, 2),
        'item_count' : len(item_ids) 
    }

    model = Order.get(by='_id', value=model_id)
    checkout_form = CheckoutForm()
    checkout_form.shipping_to_state.choices = STATES
    checkout_form.shipping_to_country.choices = COUNTRIES
    if checkout_form.validate_on_submit and checkout_form.submit_order.data:
        mdict = {
            'user_id' : user._id,
            'shipping_to' : checkout_form.shipping_to.data,
            'shipping_to_country' : checkout_form.shipping_to_country.data,
            'shipping_to_state' : checkout_form.shipping_to_state.data,
            'shipping_to_zip' : checkout_form.shipping_to_zip.data,
            'payment_info' : checkout_form.payment_info.data,
            'card_number' : checkout_form.card_number.data,
            'card_csv' : checkout_form.card_csv.data,
            'card_exp' : checkout_form.card_exp.data,
            'order_data' : user.cart,
            'is_fulfilled' : 0,
        }
        try:
            mdict.update(order_summary)
            new_order = Order(mdict)
            # Order.add(new_order)
            # user.cart = ""
            # user.update(user)
            flash ('we got your order')
            print (new_order)
            return redirect( url_for('users.order_summary', model_id=new_order._id) )
        except Exception as e:
            flash ('we were unable to complete your order')
            print ("\n\n")
            print (e)
            # flash (e)
            print ("\n\n")

        return redirect( url_for('users.index') )

    return render_template('users/_checkout.html', checkout_form=checkout_form,
                                             order_summary=order_summary,
                                             inv_models=inv_models,
                                             coupon_codes=coupon_codes)

@users.route('/submit_checkout', methods=['GET', 'POST'])
def submit_checkout():
    flash ('we got your order')
    return (redirect(url_for('users.index')))


@users.route('/delete_item/<string:model_id>', methods=['GET', 'POST'])
def delete_cart_item (model_id):
    return redirect( url_for('users.cart'))


@users.route('/order_summary/<string:model_id>')
def order_summary(model_id):
    model = Order.get(by='_id', value=model_id)
    return render_template('users/_order_summary.html', model=model)


@users.route('/user_order/<string:model_id>')
def user_orders(model_id):
    pass
