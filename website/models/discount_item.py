from website.models.master import Model


class DiscountItem (Model):
    mtype = 'discout_item'
    tablename = 'discount_items'

    @classmethod
    def get_insert_statement (cls, model):
        """ 
        Returns the DB statement that
        inserts models in this table
        """
        statement = (f"""
        INSERT INTO {model.tablename}
            (_id, discount_item_id, discount_rate,
            start_date, expire_date)
        VALUES
            ('{model._id}', '{model.discount_item_id}',
            '{model.discount_rate}', '{model.start_date}',
            '{model.expire_date}')
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
                        discount_item_id varchar(30) NOT NULL,
                        discount_rate int,
                        start_date datetime,
                        expire_date datetime,
                        upldate datetime DEFAULT CURRENT_TIMESTAMP(),
                        moddate datetime DEFAULT CURRENT_TIMESTAMP(),
                        FOREIGN KEY (discount_item_id) REFERENCES inventory(_id)
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
            discount_rate = {model.discount_rate},
            start_date = {model.start_date},
            expire_date = {model.expire_date},
            moddate = CURRENT_TIMESTAMP()
        WHERE
            _id = "{model._id}"
        """)
        
        return statement


    def __init__(self, mdict):
        super().__init__(mdict)
        self.discount_item_id = mdict['discount_item_id']
        self.discount_rate = mdict['discount_rate']
        self.start_date = mdict['start_date']
        self.expire_date = mdict['expire_date']