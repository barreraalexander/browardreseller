from website import db
from website.models.item import Item
from website.models.order import Order
from website.blueprints.main.components import ItemFlexy
from website.blueprints.main.forms import AddtoCart
from website.models.sale import Sale
from website.models.manager import Manager
from website.models.user import User
from flask import render_template, url_for,\
                  redirect, request, Blueprint
from flask_login import current_user


main = Blueprint ('main', __name__)

@main.route ("/", methods=["GET", "POST"])
def index ():
    models = Item.get(getall=True)
    
    flexs = [ ItemFlexy.get_model_flexy(model) \
            for model in models ]

    return render_template('_index.html', models=models, flexs=flexs)

@main.route ("/inventory/<string:model_id>", methods=["GET", "POST"])
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

    return render_template('_inv_item.html', model=model, form=form)

