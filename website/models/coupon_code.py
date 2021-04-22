from website.models.master import Model
import json

class CouponCode (Model):
    mtype = 'coupon_code'
    tablename = 'coupon_codes'

    @classmethod
    def get_insert_statement (cls, model):
        """ 
        Returns the DB statement that
        inserts models in this table
        """
        statement = (f"""
        INSERT INTO {model.tablename}
            (_id, coupon_code, discount_rate,
            start_date, expire_date)
        VALUES
            ('{model._id}', '{model.coupon_code}',
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
                        coupon_code varchar(30),
                        discount_rate int,
                        start_date datetime,
                        expire_date datetime,
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
        statement = (f"""UPDATE inventory
        SET 
            coupon_code = {model.coupon_code},
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
        self.coupon_code = mdict["coupon_code"]
        self.discount_rate = mdict["discount_rate"]
        self.start_date = mdict['start_date']
        self.expire_date = mdict['expire_date']


    @property
    def as_dict (self):
        return {
            '_id' : self.id,
            'coupon_code' : self.coupon_code,
            'discount_rate' : self.discount_rate,
        }


    def __str__(self):
        return (f"""
        ID: {self._id}
        Coupon Code: {self.coupon_code}
        Discount Rate: {self.discount_rate}
        Start Date: {self.start_date}
        End Date: {self.expire_date}
        """)