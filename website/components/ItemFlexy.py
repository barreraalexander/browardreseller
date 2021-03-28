from flask import Markup, url_for, redirect
from website.models.item import Item

def component(model):
    img_src = url_for('static', filename=f'images/item_images/{model._id}/{model.imgfiles[0]}')
    a_src = url_for('users.inv_item', model_id=model._id)
    
    return Markup(f""" 
    <div class='item_flexy_ctnr'>
        <img src={img_src} alt={model.name}>
        <a href={a_src}>
            <p>
                {model.name}
            </p>
        </a>
        <p class='flex_item_price'>
            ${model.selling_price}
        </p>
        <p class='flex_item_shipping'>
            Shipping: ${model.shipping_price}
        </p>
        <button class="btn_filled" onclick=submitAdd('{model._id}')>
            ADD TO CART
        </button>
    </div>
            """)