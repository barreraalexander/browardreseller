from website.models.master import Model


class Order (Model):
    mtype = 'order'
    tablename = 'orders'

    @classmethod
    def get_insert_statement (cls, model):
        """ 
        Returns the DB statement that
        inserts models in this table
        """
        statement = (f"""
        INSERT INTO {model.tablename}
            (_id, is_fulfilled, order_data,
            payment_info, shipping_to, user_id )
        VALUES
            ('{model._id}', {model.is_fulfilled},
            '{model.order_data}', '{model.payment_info}',
            '{model.shipping_to}', '{model.user_id}')
        """)
        return statement


    @classmethod
    def get_table_statement(cls):
        """
        Returns the DB statement that
        creates this model's table
        """
        statement = (f"""
        CREATE TABLE {cls.tablename} (
            _id varchar(30) PRIMARY KEY,
            is_fulfilled int,
            order_data text,
            payment_info varchar(100),
            shipping_to text,
            user_id varchar(30),
            upldate datetime DEFAULT CURRENT_TIMESTAMP(),
            moddate datetime DEFAULT CURRENT_TIMESTAMP(),
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
        statement = (f""" UPDATE orders
        SET
            is_fulfilled = {model.is_fulfilled},
            order_data = "{model.order_data}",
            shipping_to = "{model.shipping_to}",
            moddate = CURRENT_TIMESTAMP()
        WHERE
            _id = "{model._id}"        
        """)
        return statement

#//SECTION: __init__
    def __init__(self, mdict):
        super().__init__(mdict)
        self.is_fulfilled = mdict['is_fulfilled']
        self.order_data = mdict['order_data']
        self.payment_info = mdict['payment_info']
        self.shipping_to = mdict['shipping_to']
        self.user_id = mdict['user_id']

    def __str__(self):
        return (f"""
        ID: {self._id}
        IS FULFILLED: {self.is_fulfilled}
        ORDER: {self.order_data}
        PAYMENT INFO: {self.payment_info}
        SHIPPING TO: {self.shipping_to}
        USER ID: {self.user_id}
        DATE UPLOADED: {self.upldate}
        LAST MODIFIED: {self.moddate}
        """)
