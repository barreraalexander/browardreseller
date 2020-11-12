from browardreseller import db
from secrets import token_hex
from datetime import datetime


class Model:
    mtype = 'model'
    tablename = None

    # !! CLASSMETHODS # !!
    @classmethod
    def add (cls, model):
        """ Model.add(model) inserts a new model
        into the databse. """
        ModelObj = cls._Model__getobj ()
        insert_dict = ModelObj.get_insert_statement (model)
        db.insert(insert_dict)

    @classmethod
    def get (cls, by='', value='', getrandom=False, getall=False, getmany=False):
        """
        returns model object(s) 
        **by specifies the column to search

        **value specifies the value to search for in 'by'

        **getrandom=True always returns 1 random model from the table
        
        **getall=True returns all of the models in the table
        
        **getmany=True returns all of the models in the
                       table that match the query
        """
        ModelObj = cls._Model__getobj ()

        if getmany:
            records = db.get(ModelObj.tablename, col=by,
                        value=value, getmany=True)
            models = [ModelObj(record) for record in records]
            return models

        if getall:
            records = db.get(ModelObj.tablename, getall=True)
            models = [ModelObj(record) for record in records]
            return models


        record = db.get(ModelObj.tablename, col=by, value=value, getrandom=getrandom)

        if record is None:
            return None
        
        model = ModelObj (record)
        return model

    @classmethod
    def mk_table (cls):
        """ creates the model's
        complementary table """
        ModelObj = cls._Model__getobj ()
        mk_table_statement = ModelObj.get_table_statement()
        db.create_table (mk_table_statement)
        

    @classmethod
    def update (cls, model):
        """ updates a model in the db.
        Model.update(model) where model
        already exists in the db. """
        ModelObj = cls._Model__getobj ()
        update_statement = ModelObj.get_update_statement (model)
        db.update(update_statement)

    @classmethod
    def __getobj (cls):
        return cls

#//SECTION:  STATIC METHODS
    @staticmethod
    def remove (model):
        """ model is deleted from the db,
        Model.remove(model) where model
        already exists in the db. """
        db.remove(model)


#//SECTION: __init__
    def __init__(self, mdict):
        self._id = ""
        self.id = "" #accounts for some programs that use ._id as a built in
        self.imgfiles = ""
        self.updlate = ""
        self.__checkdict (mdict)

    def __checkdict (self, mdict):
        try:
            self._id = mdict['_id']
            self.id = mdict ['_id']
        except Exception as setid:
            self._id = token_hex(8)
            self.id = token_hex(8)
        
        try:
            self.imgfiles =  mdict['imgfiles']
        except Exception as setimgfile:
            self.imgfiles = None

        try:
            self.upldate = mdict ['upldate']
        except Exception as setupldate:
            self.upldate = None

        try:
            self.rating = mdict ['rating']
        except Exception as setupldate:
            self.rating = 0


























# class Model:
#     mtype = 'model'
#     tablename = None
#     def __init__(self, mdict):
#         self._id = ""
#         self.id = "" #accounts for some programs that use ._id as a built in
#         self.imgfile = ""
#         self.updlate = ""
#         self.__checkdict (mdict)

#     def __checkdict (self, mdict):
#         if mdict == None:
#             return None

#         try:
#             self._id = mdict['_id']
#             self.id = mdict ['_id']
#         except Exception as setid:
#             self._id = token_hex(14)
        
#         try:
#             self.imgfile =  "default.jpg"
#         except Exception as setimgfile:
#             self.imgfile = "default.jpg"

#         try:
#             self.upldate = mdict ['upldate']
#         except Exception as setupldate:
#             self.upldate = datetime.utcnow()


#     @classmethod
#     def get (cls, by='', value='', getrandom=False, getall=False, getmany=False):
#         ModelObj = cls._Model__getobj ()

#         if getmany:
#             records = db.get(ModelObj.tablename, col=by,
#                         value=value, getmany=True)
#             models = [ModelObj(record) for record in records]
#             return models

#         if getall:
#             records = db.get(ModelObj.tablename, getall=True)
#             models = [ModelObj(record) for record in records]
#             return models


#         record = db.get(ModelObj.tablename, col=by, value=value, getrandom=getrandom)
#         model = ModelObj (record)
#         return model
#         # if record:
#         #     model = ModelObj (record)
#         #     return model
#         # return "nope"

#     @staticmethod
#     def add (model):
#         try:
#             db.insert (model)
#             return True
#         except Exception as modelinsert:
#             print (f"db-model-insert-error for {model}")
#             return False

#     @staticmethod
#     def remove (model):
#         try:
#             db.remove (model)
#             return True
#         except Exception as modelremove:
#             print (f'db-model-remove-error for {model}')
#             return False

#     @staticmethod
#     def update (model):
#         db.update (model)
#         try:
#             db.update (model)
#             return True
#         except Exception as modelupdate:
#             print (f'db-model-update-error for {model}')
#             return False

#     #!! HELPERS !!#
#     @classmethod
#     def __getobj (cls):
#         return cls

