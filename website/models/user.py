from website.models.master import Model
from website.models.item import Item
from flask_login import UserMixin
from website import login_user

@login_user.user_loader
def load_user (_id):
    print ('ran user loader')
    return User.get(by="_id", value=_id)

class User (Model, UserMixin):
    mtype ='user'
    tablename ='users'
#//SECTION: DB METHODS
    @classmethod
    def get_insert_statement(cls, model):
        """ 
        Returns the DB statement that
        inserts models in this table
        """
        statement = (f"""
        INSERT INTO {model.tablename}
            (_id, address, cart, email, ip_address)
        VALUES
            ('{model._id}', '{model.address}', '{model.cart}',
            '{model.email}', '{model.ip_address}')
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
            address varchar(100),
            cart text,
            email varchar(100),
            ip_address varchar(30) UNIQUE,
            upldate datetime DEFAULT CURRENT_TIMESTAMP(),
            moddate datetime DEFAULT CURRENT_TIMESTAMP()
            )""")
        return statement


    @classmethod
    def get_update_statement(cls, model):
        """ 
        Returns the DB statement that
        updates models in this table
        """
        statement = (f""" UPDATE users
        SET
            address = "{model.address}",
            cart = "{model.cart}",
            email = "{model.email}",
            ip_address = "{model.ip_address}",
            moddate = CURRENT_TIMESTAMP()
        WHERE
            _id = "{model._id}"
        """)
        return statement
#//SECTION: OTHER METHODS
    @staticmethod
    def get_temp_user (ip_requesting):
        mdict = {
            'address' : None,
            'cart': '',
            'email':None,
            'ip_address' : ip_requesting
        }
        user = User(mdict)
        return user


#//SECTION: __init__
    def __init__(self, mdict):
        super().__init__(mdict)
        self.address = mdict['address']
        self.cart = mdict['cart']
        self.email = mdict['email']
        self.ip_address = mdict['ip_address']

    def cart_as_ls(self):
        item_ids = self.cart.split('$')
        for item in item_ids:
            if item == '':
                item_ids.remove(item)
        return item_ids

    @property
    def cart_items(self):
        pass


    def __str__(self):
        return (f"""
        ID: {self._id}
        ADDRESS: {self.address}
        EMAIL: {self.email}
        IP ADDRESS: {self.ip_address}
        DATE UPLOADED: {self.upldate}
        LAST MODIFIED: {self.moddate}
        """)