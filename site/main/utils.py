import secrets
import os
from PIL import Image
from flask import current_app

# PHOTOS_PATH = os.path.join (current_app.root_path, 'static/images/item_images')
# PHOTOS_PATH = "browardreseller/static/images/item_images"


def make_folder (model_id):
    try:            
        PHOTOS_PATH = os.path.join (current_app.root_path, 'static/images/item_images')
        os.chdir(PHOTOS_PATH)
        os.mkdir(model_id)

        MODEL_PATH = os.path.join (PHOTOS_PATH, model_id)
        os.chdir(MODEL_PATH)
        os.mkdir("thumbnails")
    except:
        print ("dir has already been made")
        
def save_pictures (form_pictures, model_id):
    PHOTOS_PATH = os.path.join (current_app.root_path, 'static/images/item_images')
    "saves pictures and returns a list of filenames"
    pic_filenames = []
    make_folder(model_id)
    for i, picture in enumerate(form_pictures):
        _, f_ext = os.path.splitext(picture.filename)
        picture_fn = model_id+"_"+str(i)+f_ext
        picture_path = os.path.join(PHOTOS_PATH, model_id, picture_fn)
        thumbnail_path = os.path.join (PHOTOS_PATH, model_id, "thumbnails", picture_fn)

        i = Image.open (picture)
        # w = i.width - (i.width * .40)
        # h = i.height - (i.height * .40)
        # i.size
        # i.resize(w, h)
        i.save(picture_path)

        output_size = (180, 180)
        i.thumbnail(output_size)
        i.save(thumbnail_path)

        pic_filenames.append (picture_fn)

    return pic_filenames





