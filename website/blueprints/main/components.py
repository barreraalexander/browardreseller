from flask import Markup, url_for, redirect
from website.models.item import Item


class Component:
    def __init__(self):
        pass

class ItemFlexy:
    @staticmethod
    def get_model_flexy (model):
        img_src = url_for('static', filename=f'images/item_images/{model._id}/{model.imgfiles[0]}')
        a_src = url_for('main.inv_item', model_id=model._id)
        
        return Markup(f""" 
        <div class='item_flexy_ctnr'>
            <img src={img_src} alt={model.name}>
            <a href={a_src}>
                <p>
                    {model.name}
                </p>
            </a>
            <p style='color:green;margin-left:5em;margin-top:1em;'> ${model.selling_price} </p>
        </div>
                """)
    def __init__(self):
        pass


class ItemDiv:
    @staticmethod
    def get_sell_div(model):
        img_src = url_for('static', filename=f'images/item_images/{model._id}/thumbnails/{model.imgfiles[0]}')
        a_src = url_for('main.inv_item', model_id=model._id)
        
        component = Markup(f"""
        <h5> {model.name} </h5>
        <div class='sell_divs_ctnr'>
            <div class='sell_img_div'>
                <img src="{img_src}" alt="merch_img">
            </div>

            <div>
                <p class='sell_head'>
                    Quantity
                </p>
                <p>
                    Quantity
                </p>
            </div>

            <div>
                <p class='sell_head'>
                    Total
                </p>
                <p>
                    {model.selling_price}
                </p>
            </div>
         

            <div>
                <button id="remove_btn_shown"  onclick=submitRemove("{model._id}") class="remove_button">
                    REMOVE
                </button>
            </div>
        </div>
        <hr>
        """)
        return component