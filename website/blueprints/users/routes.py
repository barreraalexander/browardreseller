from website import bcrypt, db
from website.blueprints.users.forms import OrderForm, RemoveItemForm, CheckoutForm
# from website.blueprints.main.components import ItemDiv
from website.components.ItemDiv import component as item_div_cmpnt
from website.components.ItemFlexy import component as item_flexy_cmpnt
# from website.components.ItemDiv import component as item_div_cmpnt
from website.models.item import Item
from website.models.order import Order
from website.models.sale import Sale
from website.models.user import User
from flask import render_template, url_for,\
                  redirect, request, Blueprint

from flask_login import current_user
from website.blueprints.users.forms import AddtoCart
from datetime import datetime, timedelta

# from website.blueprints.main.components import ItemFlexy
# from website.models.manager import Manager




users = Blueprint ('users', __name__)


@users.route ("/", methods=["GET", "POST"])
def index ():
    models = Item.get(getall=True)
    
    flexs = [ item_flexy_cmpnt(model) \
            for model in models ]

    promo_item = Item.get(by="_id", value="fa9f2a892e7239c9a6086539d776")
    slider_item = Item.get(by="_id", value="fe6cf011aae691791ea17c9834f8")

    slider_item.reduction = 30
    slider_item.reduced_price = slider_item.selling_price - (round(slider_item.selling_price * slider_item.reduction/100, 2))


    slider_item.sale_start = datetime(year=2021, month=1, day=6)
    slider_item.sale_end = datetime(year=2021, month=2, day=26)
    slider_item.sale_daysleft = str(slider_item.sale_end - datetime.now()).split(',')[0].split(' ')[0]

    return render_template('users/_index.html', flexs=flexs, models=models, promo_item=promo_item, slider_item=slider_item)

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
            return redirect( url_for('main.index') )

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


    sell_divs = [ItemDiv.get_sell_div(model) for model in models]
    return render_template('users/_cart.html', title='Cart', models=models, cart=user.cart, order_form=order_form, remove_form=remove_form, sell_divs=sell_divs)

@users.route('/checkout/<string:model_id>', methods=['GET', 'POST'])
def checkout (model_id):
    user = User.get(by='_id', value=model_id)
    item_ids = user.cart_as_ls()

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

    if checkout_form.validate_on_submit and checkout_form.submit_order.data:
        mdict = {
            'user_id' : user._id,
            'shipping_to' : checkout_form.shipping_to.data,
            'payment_info' : checkout_form.payment_info.data,
            'order_data' : user.cart,
            'is_fulfilled' : 0,
            
        }
        mdict.update(order_summary)
        new_order = Order(mdict)
        Order.add(new_order)

        print (new_order)
        return redirect( url_for('main.index') )

    return render_template('users/_checkout.html', checkout_form=checkout_form,
                                             order_summary=order_summary,
                                             inv_models=inv_models)