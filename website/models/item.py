from website.models.master import Model
from datetime import datetime

class Item (Model):
    mtype = 'item'
    tablename = 'inventory'
#//SECTION: DB METHODS
    @classmethod
    def get_insert_statement (cls, model):
            statement = (f"""
            INSERT INTO {model.tablename}
                (_id, category, c_type, brand, model_num,
                colors, size, name, obj_condition, orig_value,
                purchase_price, selling_price, shipping_price,
                stock, imgfiles) 
            VALUES
                ('{model._id}', '{model.category}',
                '{model.c_type}', '{model.brand}',
                '{model.model_num}', '{model.name}', 
                '{model.colors}', '{model.size}',
                '{model.obj_condition}', {model.orig_value},
                {model.purchase_price}, {model.selling_price},
                {model.shipping_price}, {model.stock},
                '{model.imgfiles}')
            """)
            return statement


    @classmethod
    def get_table_statement (cls):
        """
        Returns the DB statement that
        creates this model's table
        """

        statement = (f"""
        CREATE TABLE {tablename}
            (_id varchar(30) PRIMARY KEY,
            category varchar(100),
            c_type varchar(100),
            brand varchar(100),
            model_num varchar (100),
            name varchar(100),
            colors text,
            size varchar (50),
            obj_condition varchar(100),
            orig_value float DEFAULT 0,
            purchase_price float DEFAULT 0,
            selling_price float DEFAULT 0,
            shipping_price float DEFAULT 0,
            stock int DEFAULT 0,
            imgfiles text,
            upldate datetime DEFAULT CURRENT_TIMESTAMP(),
            moddate datetime DEFAULT CURRENT_TIMESTAMP()
                        )""")                        
        return statement

    @classmethod
    def get_update_statement (cls, model):
        """ 
        Returns the DB statement that
        updates models in this table
        """
        statement = (f""" UPDATE inventory
        SET 
            category = "{model.category}",
            c_type = "{model.c_type}",
            brand = "{model.brand}",
            model_num = "{model.model_num}",
            name = "{model.name}",
            colors = "{model.colors}",
            size = "{model.size}",
            obj_condition = "{model.obj_condition}",
            orig_value = {model.orig_value},
            purchase_price = {model.purchase_price},
            selling_price = {model.selling_price},
            shipping_price = {model.shipping_price},
            stock = {model.stock},
            imgfiles = "{model.imgfiles}",
            moddate = CURRENT_TIMESTAMP()
        WHERE
            _id = "{model._id}"
        """)
        return statement


    def __init__(self, mdict):
        super().__init__(mdict)
        #item information
        self.category = mdict["category"]
        self.c_type = mdict["c_type"]
        self.brand = mdict["brand"]
        self.model_num = mdict["model_num"]
        self.colors = mdict ["colors"]
        self.size = mdict["size"]
        self.name = mdict["name"]
        self.obj_condition = mdict["obj_condition"]
        #item pricing        
        self.orig_value = mdict["orig_value"]
        self.purchase_price = mdict["purchase_price"]
        self.selling_price = mdict["selling_price"]
        self.shipping_price = mdict["shipping_price"]
        self.stock = mdict["stock"]

        #sell status
        self._set_defaults (mdict)
        self._set_details (mdict)

    def style_for_web (self):
        try:        
            self.upldate = str(self.upldate)[0:10]
            self.orig_value = "{:,.2f}".format(self.orig_value)
            self.purchase_price = "{:,.2f}".format(self.purchase_price)
            self.selling_price = "{:,.2f}".format(self.selling_price)
            self.shipping_price = "{:,.2f}".format(self.shipping_price)
        except:
            pass


    def _set_defaults (self, mdict):
        try:
            csv_imgfiles = mdict["imgfiles"]
            self.imgfiles = csv_imgfiles.split(",")

        except:
            self.imgfiles = "None"
    

        try:
            csv_colors = mdict["colors"]
            self.colors = csv_colors.split(",")
        except:
            self.colors = "None"

        
        try:
            self.model_num = mdict["model_num"]
        except:
            self.model_num = "None"

    def _set_details (self, mdict):        
        try:
            self.size = mdict["size"]
        except:
            self.size = "None"

        try:
            self.release_year = mdict["release_year"]
        except:
            self.release_year = "None"

    @property
    def details (self):
        details = []

        if self.obj_condition == "new" or self.obj_condition=="unopened":
            details.append(self.obj_condition.upper())
        
        details.append (self.brand.upper())
        details.append (self.name)

        model_num = f"[SKU:{self.model_num}]"
        details.append (model_num)
        
        if self.colors:     
            colors = ""
            for color in self.colors:
                colors += color+"/"
            colors = colors[0:-1]            
            s_colors = f"({colors})"

            details.append (s_colors)
        
        details.append (self.size)

        for detail in details:
            if detail == None:
                details.remove(detail)

        details = " ".join(details)

        return details


    def size_asdict(self, key=None):
        size, gender, country = self.size.split(" ")

        dict = {
            'size': size,
            'gender': gender,
            'country': country
        }

        if key:
            return dict[key]

        return dict

    

    @staticmethod
    def get_sold ():
        models = Item.get (by="sold", value="True", getmany=True)
        return models

    @staticmethod
    def get_stock ():
        models = Item.get (by="sold", value="False", getmany=True)
        return models


    @staticmethod
    def item_count ():
        pass


    @staticmethod
    def get_items_totals(models):
        """
        Returns a dict with 2 values:
        The total 
        """
        purchase_price = 0
        selling_price = 0
        shipping_price = 0
        orig_value = 0
        for model in models:
            if model:                    
                purchase_price += model.purchase_price
                selling_price += model.selling_price
                shipping_price += model.shipping_price
                orig_value += model.orig_value
        return {
            'purchase_price': round(purchase_price, 2),
            'selling_price': round(selling_price, 2),
            'shipping_price': round(shipping_price/len(models), 2) + (1 * len(models)),
            'orig_value': round(orig_value, 2),
        }
    

    @staticmethod
    def get_models (data):
        """
        accepts raw cart data from the database ie,
        dollar separated values, model1__id$model2_id
        """
        id_ls = data.split('$')
        models = [ Item.get(by='_id', value=_id) \
                 for _id in id_ls
                 if _id != ""]
        
        return models

    def __str__(self):
        return f""" 
                ID: {self._id}
                Name: {self.name}
                """