from browardreseller.models.master import Model

class Sale (Model):
    mtype = 'sale'
    tablename = 'sales'
#//SECTION: DB METHODS
    @classmethod
    def get_insert_statement (cls, model):
        statement = (f"""INSERT INTO {model.tablename}
        (_id, item_id, purchase_price, selling_price,
        shipping_price, uploaded_to, site_sold)
        VALUES (%s, %s, %s, %s, %s, %s, %s)""")
        record = (model._id, model.item_id,
                model.purchase_price, model.selling_price,
                model.shipping_price, model.uploaded_to,
                model.site_sold)   
            
        return {
            'statement':statement,
            'record':record,
        }

    @classmethod
    def get_table_statement (cls):
        """ Returns the DB statement that
            creates this model's table"""

        statement = (f"""CREATE TABLE {tablename}
                        (_id varchar(30) PRIMARY KEY,
                        item_id varchar(30),
                        purchase_price float,
                        selling_price float,
                        shipping_price float,
                        uploaded_to text,
                        site_sold varchar(100),
                        upldate datetime DEFAULT CURRENT_TIMESTAMP(),
                        FOREIGN KEY (item_id) REFERENCES inventory(_id)
                        ON UPDATE CASCADE
                        )""")
        return statement

    @classmethod
    def get_update_statement (cls, model):
        """ Returns the DB statement that
            updates models in this table"""
        statement = (f"""UPDATE inventory
        SET 
            category = "{model.category}",
            c_type = "{model.c_type}",
            brand = "{model.brand}",
            model_num = "{model.model_num}",
            colors = "{model.colors}",
            size = "{model.size}",
            obj_condition = "{model.obj_condition}",
            name = "{model.name}",
            orig_value = {model.orig_value},
            selling_price = {model.selling_price},
            shipping_price = {model.shipping_price},
            uploaded = "{model.uploaded}",
            uploaded_to = "{model.uploaded_to}"
        WHERE
            _id = "{model._id}" """)
        
        return statement

    def __init__(self, mdict):
        super().__init__(mdict)
        self.item_id = mdict ["item_id"]
        self.purchase_price = mdict["purchase_price"]
        self.selling_price = mdict["selling_price"]
        self.shipping_price = mdict["shipping_price"]
        self.uploaded_to = mdict["uploaded_to"]
        self.site_sold = mdict["site_sold"]
        # self.upldate = mdict ["upldate"]


    def style_for_web (self):
        try:        
            self.upldate = str(self.upldate)[0:10]
            self.purchase_price = "{:,.2f}".format(self.purchase_price)
            self.selling_price = "{:,.2f}".format(self.selling_price)
            self.shipping_price = "{:,.2f}".format(self.shipping_price)
        except:
            pass


    
