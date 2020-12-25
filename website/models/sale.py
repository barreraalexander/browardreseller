from website.models.master import Model

class Sale (Model):
    mtype = 'sale'
    tablename = 'sales'
#//SECTION: DB METHODS
    @classmethod
    def get_insert_statement (cls, model):
        """ 
        Returns the DB statement that
        inserts models in this table
        """
        statement = (f"""
        INSERT INTO {model.tablename}
            (_id, manager_id, order_id,
            user_id, selling_price,
            shipping_price, selling_cost,
            shipping_cost)
        VALUES
            ('{model._id}', '{model.manager_id}',
            '{model.order_id}', '{model.user_id}',
            {model.selling_price}, {model.shipping_price},
            {model.selling_cost}, {model.shipping_cost})
        """)
        return statement

    @classmethod
    def get_table_statement (cls):
        """
        Returns the DB statement that
        creates this model's table
        """
        statement = (f"""
        CREATE TABLE {cls.tablename}
                        (_id varchar(30) PRIMARY KEY,
                        manager_id varchar(30),
                        order_id varchar(30),
                        user_id varchar(30),
                        selling_price float,
                        shipping_price float,
                        selling_cost float,
                        shipping_cost float,
                        upldate datetime DEFAULT CURRENT_TIMESTAMP(),
                        moddate datetime DEFAULT CURRENT_TIMESTAMP(),
                        FOREIGN KEY (manager_id) REFERENCES managers(_id)
                            ON UPDATE CASCADE,
                        FOREIGN KEY (order_id) REFERENCES orders(_id)
                            ON UPDATE CASCADE,
                        FOREIGN KEY (user_id) REFERENCES users(_id)
                            ON UPDATE CASCADE
                        )""")
        return statement

    @classmethod
    def get_update_statement (cls, model):
        """ 
        Returns the DB statement that
        updates models in this table
        """
        statement = (f"""UPDATE inventory
        SET 
            manager_id = "{model.manager_id}",
            order_id = "{model.order_id}",
            user_id = "{model.user_id}",
            selling_price = {model.selling_price},
            shipping_price = {model.shipping_price},
            selling_cost = {model.selling_cost},
            shipping_cost = {model.shipping_cost},
            moddate = CURRENT_TIMESTAMP()
        WHERE
            _id = "{model._id}"
        """)
        
        return statement

    def __init__(self, mdict):
        super().__init__(mdict)
        self.manager_id = mdict ["manager_id"]
        self.order_id = mdict ["order_id"]
        self.user_id = mdict ["user_id"]
        self.selling_price = mdict["selling_price"]
        self.shipping_price = mdict["shipping_price"]
        self.selling_cost = mdict["selling_cost"]
        self.shipping_cost = mdict["shipping_cost"]

