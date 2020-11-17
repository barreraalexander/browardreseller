from flask import Markup, url_for, redirect
from website.models.item import Item


class Component:
    def __init__(self):
        pass

class ItemFlexy():
    @staticmethod
    def get_model_flexy (model):
        img_src = url_for('static', filename=f'images/item_images/{model._id}/thumbnails/{model.imgfiles[0]}')
        a_src = url_for('main.inv_item', item_id=model._id)
        
        return Markup(f""" 
        <div class='item_flexy_ctnr'>
            <img src={img_src} alt={model.name}>
            <a href={a_src}><p> {model.name} </p></a>
            <p style='color:green;margin-left:5em;margin-top:1em;'> ${model.selling_price} </p>
        </div>
                """)

    def __init__(self):
        pass
        