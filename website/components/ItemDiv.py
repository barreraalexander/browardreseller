from flask import Markup, url_for, redirect
from website.models.item import Item


def component(model):
    def get_sell_div(model):
        img_src = url_for('static', filename=f'images/item_images/{model._id}/thumbnails/{model.imgfiles[0]}')
        a_src = url_for('users.inv_item', model_id=model._id)
        
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