from website.models.master import Model
from flask_login import UserMixin
from website import login_manager
from secrets import token_hex
from datetime import datetime

@login_manager.user_loader
def load_user (_id):
    return Manager.get(by="_id", value=_id)
 

#//all users will be temp users
class Manager (Model, UserMixin):
    mtype='manager'
    tablename='managers'

#//SECTION: DB METHODS
    @classmethod
    def get_insert_statement(cls, model):
        """ 
        Returns the DB statement that
        inserts models in this table
        """
        statement = (f"""
        INSERT INTO {model.tablename}
            (_id, f_name, l_name, email, password)
        VALUES
            ('{model._id}', '{model.f_name}', '{model.l_name}',
            '{model.email}', '{model.password}')
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
            f_name varchar(30),
            l_name varchar(30),
            email varchar(100) UNIQUE,
            password varchar(100),
            goal int DEFAULT 0,
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
        statement = (f""" UPDATE managers
        SET
            f_name = "{model.f_name}",
            l_name = "{model.l_name}",
            email = "{model.email}", 
            password = "{model.password}",
            goal = "{model.goal}", 
            moddate = CURRENT_TIMESTAMP()
        WHERE
            _id = "{model._id}"
        """)
        return statement

    def __init__(self, mdict):
        super().__init__(mdict)
        self.f_name = mdict ['f_name']
        self.l_name = mdict ['l_name']
        self.email = mdict ['email']
        self.password = mdict ['password']
        self.goal = mdict ['goal']

    def __str__(self):
        return (f"""
        FIRST NAME: {self.f_name}
        LAST NAME: {self.l_name}
        EMAIL: {self.email}
        PASSWORD: {self.password}
        """)