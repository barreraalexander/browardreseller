from website import db, bcrypt
from website.blueprints.managers.forms import NewItemForm, NewSaleForm, \
                                        LoginForm, RegisterForm, \
                                        FulfillForm, SetGoalForm
from website.blueprints.managers.utils import save_pictures
from website.models.item import Item
from website.models.user import User
from website.models.manager import Manager
from website.models.order import Order
from website.models.sale import Sale
from website.blueprints.managers import CATEGORIES, CONDITIONS, COLORS
from flask_login import current_user
from os import path
from flask import render_template, url_for, flash,\
                    redirect, request, Blueprint
from flask_login import login_user,logout_user, current_user, login_required

managers = Blueprint ('managers', __name__)


@managers.route('/backstage/<user_id>/add_item', methods=['GET', 'POST'])
@login_required
def add_item (user_id):
    form = NewItemForm ()
    form.category.choices = CATEGORIES
    form.colors.choices = COLORS
    form.obj_condition.choices = CONDITIONS

    if request.method=="POST":
        if form.submit_new_item.data and form.validate_on_submit:
            new_item = Item(form.data)
            new_item.uploaded_to = "$".join(form.uploaded_to.data)
            new_item.colors = "$".join(form.colors.data)
            new_item.imgfiles = 'default.jpg'

            # if form.imgfiles.data:
            #     pic_filenames = save_pictures(form.imgfiles.data, new_item._id)
            #     new_item.imgfiles = ",".join(pic_filenames)
            #     pass

            Item.add(new_item)
            print ('ran')           
            flash (f"Added {new_item.name} to Inventory {form.obj_condition.data} {form.uploaded_to.data} {form.c_type.data}")
            return redirect(url_for('managers.inventory', user_id=current_user._id))
    return render_template('managers/_add_item.html', form=form)




@managers.route ('/backstage', methods=['GET', 'POST'])
def backstage():
    if current_user.is_authenticated:
        return redirect(url_for('managers.home', user_id=current_user.id))
    
    login_form = LoginForm()
    register_form = RegisterForm()
    if request.method == 'POST':    
        if login_form.validate_on_submit and login_form.submit_login.data:
            manager = Manager.get(by='email', value=login_form.login_email.data)
            if manager and bcrypt.check_password_hash (manager.password, login_form.login_password.data):
                x = login_user (manager, remember=True)
                print ( 'Log In Status:' ,x)
                next_page = request.args.get('next')
                return redirect(url_for('managers.backstage'))
            else:
                print ('password wrong')
                return redirect(url_for('managers.backstage'))
    
        elif register_form.validate_on_submit and register_form.submit_register.data:
            mdict = {
                'f_name' : register_form.f_name.data,
                'l_name' : register_form.l_name.data,
                'email' : register_form.register_email.data,
                'password' : register_form.register_password.data,
                'goal' : 0,
            }
            new_manager = Manager(mdict)
            enc_password = bcrypt.generate_password_hash(new_manager.password).decode('utf8')
            new_manager.password = enc_password
            try:
                Manager.add(new_manager)
                x = login_user (new_manager, remember=True)
                print ( 'Log In Status:' , x)
                next_page = request.args.get('next')
                return redirect(url_for('managers.backstage'))
            except Exception as err:
                print (err)
            finally:
                return redirect(url_for('managers.backstage'))

    print (current_user.is_authenticated)
    return render_template ('managers/_backstage.html', login_form=login_form, register_form=register_form)


@managers.route('/backstage/u/<user_id>/home', methods=['POST', 'GET'])
@login_required
def home(user_id):
    open_orders = Order.get(by='is_fulfilled', value=0, getmany=True)
    for order in open_orders:
        user = User.get(by='_id', value=order.user_id)
        order.user = user
        form = SetGoalForm()

        order.order_total = 0
        
        items = Item.get_models(order.order_data)
        for item in items:
            order.order_total += item.selling_price

        if request.method=="POST":
            if form.validate_on_submit and form.submit_goal.data:
                current_user.goal = form.goal.data
                Manager.update(current_user)
                print ('ran')
                return redirect(url_for('managers.home', user_id=current_user._id))

    sales = Sale.get(by='manager_id', value=current_user._id, getmany=True)
    current_user.sales_total = 0
    for sale in sales:
        current_user.sales_total += sale.selling_price

    if current_user.goal != 0:
        ratio = (current_user.sales_total/current_user.goal) * 100
        current_user.perc_goal = int(ratio)
    else:
        current_user.perc_goal = 0

    return render_template('managers/_home.html', open_orders=open_orders, form=form)


@managers.route ('/backstage/<user_id>/inventory')
@login_required
def inventory (user_id):
    models = Item.get(getall=True)
    sorted_models = []
    return render_template('managers/_inventory.html', models=models, CATEGORIES=CATEGORIES)



@managers.route('/backstage/<user_id>/inventory/<string:model_id>', methods=['GET', 'POST'])
@login_required
def inv_item_m(model_id, user_id):
    model = Item.get(by='_id', value=model_id)
    form = NewItemForm()
    form.category.choices = CATEGORIES
    form.colors.choices = COLORS
    form.obj_condition.choices = CONDITIONS

    if request.method=="POST":
        if form.submit_new_item.data and form.validate_on_submit:
            model.category = form.category.data
            model.c_type = form.c_type.data
            model.brand = form.brand.data
            model.model_num = form.model_num.data
            model.colors = '$'.join(form.colors.data)

            model.size = form.size.data
            model.name = form.name.data
            model.obj_condition = form.obj_condition.data
            model.orig_value = form.orig_value.data
            model.purchase_price = form.purchase_price.data
            model.selling_price = form.selling_price.data
            model.shipping_price = form.shipping_price.data
            model.stock = form.stock.data

            Item.update(model)

            # if form.imgfiles.data:
            #     pic_filenames = save_pictures(form.imgfiles.data, new_item._id)
            #     new_item.imgfiles = ",".join(pic_filenames)
            #     pass

            # Item.add(new_item)
            print ('ran')           
            return redirect(url_for('managers.inventory', user_id=current_user._id))


    return render_template('managers/_inv_item.html', model=model, form=form)


@managers.route('/backstage/<user_id>/open_orders', methods=['GET'])
@login_required
def open_orders(user_id):
    models = Order.get(getall=True)
    for model in models:
        model.items = Item.get_models(model.order_data)
        model.items_totals = Item.get_items_totals (model.items)
        for item in model.items:
            print (item.name)
        # print (model.items)
    return render_template('managers/_open_orders.html', models=models)

@managers.route('/backstage/<user_id>/open_orders/<string:model_id>', methods=['GET', 'POST'])
def open_order(model_id, user_id):
    order = Order.get(by='_id', value=model_id)
    user = User.get(by='_id', value=order.user_id)
    items_ordered = Item.get_models(order.order_data)
    items_totals = Item.get_items_totals (items_ordered)
    sale = Sale.get(by="order_id", value=order._id)

    form = FulfillForm()
    if request.method=='POST':
        if form.validate_on_submit and form.submit_fulfill.data:
            order.is_fulfilled = 1
            Order.update(order)

            mdict = {
                'manager_id' : current_user._id,
                'order_id' : order._id,
                'user_id' : order.user_id,
                'selling_price': items_totals['selling_price'],
                'shipping_price': items_totals['shipping_price'],
                'selling_cost': 0,
                'shipping_cost' : 0
            }

            for item in items_ordered:
                item.sold = 1
                Item.update(item)

            new_sale = Sale(mdict)
            Sale.add(new_sale)

            return redirect(url_for('managers.open_order', model_id=order._id, user_id=user_id))

    return render_template('managers/_open_order.html', order=order,
                                            user=user, form=form,
                                            items_totals=items_totals,
                                            items_ordered=items_ordered,
                                            sale=sale)


@managers.route('/backstage/<user_id>/sales', methods=['GET'])
@login_required
def sales(user_id):
    models = Sale.get(getall=True)
    for model in models:
        model.manager = Manager.get(by='_id', value=model.manager_id)
        model.user = User.get(by='_id', value=model.user_id)
    return render_template('managers/_sales.html', models=models)


@managers.route('/backstage/<user_id>/sales/<string:model_id>', methods=['GET'])
@login_required
def sale(model_id):
    model = Sale.get(by='_id', value=model_id)
    return render_template('managers/_sale.html', model=model)


@managers.route('/backstage/<user_id>/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('managers.backstage'))
