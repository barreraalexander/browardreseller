from website import bcrypt
from website.blueprints.users.forms import OrderForm, RemoveItemForm, CheckoutForm
from website.blueprints.main.components import ItemDiv
from website.models.item import Item
from website.models.order import Order
from website.models.user import User
from flask import render_template, url_for,\
                  redirect, request, Blueprint

users = Blueprint ('users', __name__)
    
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
    return render_template('/users/_cart.html', title='Cart', models=models, cart=user.cart, order_form=order_form, remove_form=remove_form, sell_divs=sell_divs)

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

    return render_template('/users/_checkout.html', checkout_form=checkout_form,
                                             order_summary=order_summary,
                                             inv_models=inv_models)