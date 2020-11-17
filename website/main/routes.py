from os import path
from flask import render_template, url_for, flash,\
                    redirect, request, Blueprint
from website import db
from website.main.forms import NewItemForm, NewSaleForm, UploadItemForm, UploadRoloForm
from website.main.utils import save_pictures
from website.models.item import Item
from website.models.sale import Sale
# from website.utils.components import ItemFlexy
from website.main.components import ItemFlexy

# from website.webhandlers.depop import DepopManager
# from website.webhandlers.ebay import EbayManager

main = Blueprint ('main', __name__)


CATEGORIES = ['electronics','clothes','toys','dishes']
COLORS = ['black', 'white', 'red', 'green', 'yellow', 'purple', 'blue', 'grey', 'pink', 'teal', 'orange' ]
CONDITIONS = ['unopened','new','used']
RETAIL_SITES = ['ebay', 'mercari', 'depop', 'poshmark']


@main.route ("/", methods=["GET", "POST"])
def index ():
    models = Item.get(getall=True)
    
    flexs = [ ItemFlexy.get_model_flexy(model) \
            for model in models ]
    
    return render_template('_index.html', models=models, flexs=flexs)

@main.route ("/inventory")
def inventory ():
    models = Item.get_stock()
    for model in models:
        model.style_for_web()

    model_count = len(models)
    uploaded_count = len([])
    sold_count = ""
    return render_template('inventory.html', models=models, CATEGORIES=CATEGORIES)

@main.route ("/inventory/<string:item_id>", methods=["GET", "POST"])
def inv_item (item_id):
    model = Item.get(by="_id", value=item_id)
    form = NewItemForm ()
    
    form.category.choices = CATEGORIES
    form.colors.choices = COLORS
    form.obj_condition.choices = CONDITIONS
    form.uploaded_to.choices = RETAIL_SITES

    if request.method=="POST":
        if form.submit_update_item.data and form.validate_on_submit:

            updated_item = Item(form.data)
            updated_item._id = model._id
            updated_item.imgfiles = model.imgfiles


            updated_item.uploaded_to = ",".join(form.uploaded_to.data)
            updated_item.colors = ",".join(form.colors.data)



            if form.imgfiles.data:
                # pass
                try:
                    pic_filenames = save_pictures(form.imgfiles.data, updated_item._id)
                    updated_item.imgfiles = ",".join(pic_filenames)
            
                except:
                    updated_item.imgfiles = " "

            Item.update(updated_item)

            return redirect(url_for('main.inv_item', item_id=model._id))


    return render_template('_inv_item.html', model=model, form=form)


@main.route ("/sell_item/<string:item_id>",  methods=["GET", "POST"])
def sell_item (item_id):
    model = Item.get(by="_id", value=item_id)
    model.style_for_web()
    form = NewSaleForm ()
    form.site_sold.choices = RETAIL_SITES

    if form.submit_new_sale.data and form.validate_on_submit:
        model.sold = "True"
        model.selling_price = form.selling_price.data
        model.shipping_price = form.purchase_price.data
        model.site_sold = form.site_sold.data
        Item.update (model)

        new_sale = Sale (form.data)
        new_sale.uploaded_to = model.uploaded_to
        Sale.add (new_sale)
        return redirect(url_for('main._index'))



    return render_template('sell_item.html', model=model, form=form)

@main.route ("/upload_rolo", methods=["GET", "POST"])
def upload_rolo ():
    models = Item.get(by="uploaded", value="False", getmany=True)
    for model in models:
        model.style_for_web()
    form = UploadRoloForm()

    if form.validate_on_submit and form.submit_upload_item.data:
        flash (form.item_id.data)
        updated_model = Item.get(by="_id", value=form.item_id.data)
        updated_model.uploaded = "True"
        # updated_model.uploaded_to = ",".join(model.uploaded_to)
        updated_model.colors = ",".join(model.colors)
        Item.update(updated_model)
        return redirect(url_for('main.upload_rolo'))
    
    return render_template ('upload_rolo.html', models=models, form=form)


@main.route ("/sales_manager", methods=["GET", "POST"])
def sales_manager ():
    models = Sale.get(getall=True)
    item_models = [Item.get(by="_id", value= model.item_id)
                    for model in models]
    return render_template ('sales_manager.html', models=models, item_models=item_models)


@main.route ("/web_manager", methods=["GET", "POST"])
def web_manager ():
    models = Item.get(by="uploaded", value="False", getmany=True)

    form = UploadItemForm()
    form.item.choices = [(model._id, model.name) for model in models]
    form.upload_to.choices = RETAIL_SITES

    if form.submit_upload_item.data and form.validate_on_submit:

    
        # model = Item.get(by="_id", value=form.item.data)
        # for site in form.upload_to.data:
        #     if site == "depop":
        #         whandler = DepopManager()
        #         whandler.run (model)

        #     if site == "ebay":
        #         whandler = EbayManager()
        #         whandler.run(model)

            
        return redirect(url_for('main.web_manager'))

    # flash (current_app.root_path)
    return render_template('web_manager.html', form=form, models=models)


def add_item ():
    form = NewItemForm ()
    form.category.choices = CATEGORIES
    form.colors.choices = COLORS
    form.obj_condition.choices = CONDITIONS
    form.uploaded_to.choices = RETAIL_SITES

    if request.method=="POST":
        if form.submit_new_item.data and form.validate_on_submit:
            new_item = Item(form.data)
            new_item.uploaded_to = ",".join(form.uploaded_to.data)
            new_item.colors = ",".join(form.colors.data)

            if form.imgfiles.data:
                pic_filenames = save_pictures(form.imgfiles.data, new_item._id)
                new_item.imgfiles = ",".join(pic_filenames)

            Item.add(new_item)
            
            flash (f"Added {new_item.name} to Inventory {form.obj_condition.data} {form.uploaded_to.data} {form.c_type.data}")
            return redirect(url_for('main._index'))

    # flash (f"{form.__dict__}")