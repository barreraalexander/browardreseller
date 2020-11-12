from flask_mysqldb import MySQL

class DB (MySQL):
    def __init__(self, app=None):
        super().__init__(app=app)

    #!! CALLS AND QUERIES !!#
    def create_table (self, statement):
        try:    
            cur = self.connection.cursor ()
            cur.execute (statement)
            self.connection.commit ()
        except Exception as e:
            print (e)
            return e

    def get (self, tablename, col='column', value='value', getrandom=False, getall=False, getmany=False):
        statement = (f"""SELECT * FROM {tablename}
        WHERE {col} = "{value}" """)

        if getrandom is True:
            statement = (f"""SELECT * FROM {tablename}
                        ORDER BY RAND() LIMIT 1""")

        elif getall is True:
            statement = (f""" SELECT * FROM {tablename} """)
            cur = self.connection.cursor ()
            cur.execute (statement)
            records = cur.fetchall ()
            return records

        
        if getmany is True:
            cur = self.connection.cursor ()
            cur.execute (statement)
            records = cur.fetchall ()
            return records
            
        cur = self.connection.cursor ()
        cur.execute (statement)
        record = cur.fetchone ()
        return record

    # #!! INSERTS AND UPDATES !!# 
    def insert (self, statements):
        try:
            record = statements['record']
            statement = statements ['statement']
            cur = self.connection.cursor ()
            cur.execute (statement, record)
            self.connection.commit ()
        except Exception as err:
            print ('ERROR INSERTING INTO DATABASE: \n')
            print (err)

    def remove (self, model):
        statement = f"""DELETE FROM {model.tablename}
        WHERE _id = "{model._id}" """
        cur = self.connection.cursor ()
        cur.execute (statement)
        self.connection.commit()

    def update (self, statement):
        cur = self.connection.cursor()
        cur.execute (statement)
        self.connection.commit ()


if __name__=='__main__':
    pass











# from flask_mysqldb import MySQL

# class DB(MySQL):
#     def __init__(self, app=None):
#         super().__init__(app=app)

#     #!! QUERIES !!#
#     def get (self, tablename, col='column', value='value',
#             getrandom=False, getmany=False, getall=False):
        
#         statement = (f"""SELECT * FROM {tablename}
#         WHERE {col} = "{value}" """)

#         if getrandom is True:
#             statement = (f"""SELECT * FROM {tablename}
#                         ORDER BY RAND() LIMIT 1""")

#         if getall is True:
#             statement = (f""" SELECT * FROM {tablename} """)
#             cur = self.connection.cursor ()
#             cur.execute (statement)
#             records = cur.fetchall ()
#             return records

        
#         if getmany is True:
#             cur = self.connection.cursor ()
#             cur.execute (statement)
#             records = cur.fetchall ()
#             return records

#         cur = self.connection.cursor ()
#         cur.execute (statement)
#         record = cur.fetchone ()
#         return record


#     #!! INSERT UPDATE REMOVE !!#
#     def insert (self, model):
#         if model.mtype == 'item':
#             statement = (f"""INSERT INTO {model.tablename}
#             (_id, category, c_type, brand, model_num,
#             colors, size, name, obj_condition, orig_value,
#             purchase_price, selling_price, shipping_price,
#             uploaded, uploaded_to, imgfiles)
#             VALUES (%s, %s, %s, %s, %s, %s, %s, %s,
#                     %s, %s, %s, %s, %s, %s, %s, %s)""")
#             record = (model._id, model.category,
#                     model.c_type, model.brand,
#                     model.model_num, model.colors,
#                     model.size, model.name, model.obj_condition,
#                     model.orig_value, model.purchase_price,
#                     model.selling_price, model.shipping_price,
#                     model.uploaded, model.uploaded_to,
#                     model.imgfiles)
        
#         elif model.mtype == 'sale':
#             statement = (f"""INSERT INTO {model.tablename}
#             (_id, item_id, purchase_price, selling_price,
#             shipping_price, uploaded_to, site_sold)
#             VALUES (%s, %s, %s, %s, %s, %s, %s)""")
#             record = (model._id, model.item_id,
#                     model.purchase_price, model.selling_price,
#                     model.shipping_price, model.uploaded_to,
#                     model.site_sold)

        
#         cur = self.connection.cursor ()
#         cur.execute (statement, record)
#         self.connection.commit()


#     def update (self, model):
#         if model.mtype=='item':
#             statement = f"""UPDATE inventory
#             SET 
#                 category = "{model.category}",
#                 c_type = "{model.c_type}",
#                 brand = "{model.brand}",
#                 model_num = "{model.model_num}",
#                 colors = "{model.colors}",
#                 size = "{model.size}",
#                 obj_condition = "{model.obj_condition}",
# 	            name = "{model.name}",
#                 orig_value = {model.orig_value},
#                 selling_price = {model.selling_price},
#                 shipping_price = {model.shipping_price},
#                 uploaded = "{model.uploaded}",
#                 uploaded_to = "{model.uploaded_to}"
#             WHERE
#                 _id = "{model._id}" """

#         # elif model.mtype=='sale':
#         #     statement = f"""UPDATE {model.tablename}
#         #     SET 
#         #         weight = {model.weight}
#         #     WHERE
#         #         _id = "{model._id}" """

#         cur = self.connection.cursor()
#         cur.execute (statement)
#         self.connection.commit ()

#     def remove (self, model):
#         statement = f"""DELETE FROM {model.tablename} WHERE _id = "{model._id}" """
#         cur = self.connection.cursor ()
#         cur.execute (statement)
#         self.connection.commit()
    

#     def __createtable (self, tablename):
#         if tablename.lower () == 'inventory':
#             statement = (f"""CREATE TABLE {tablename}
#                             (_id varchar(30) PRIMARY KEY,
#                             category varchar(100),
#                             c_type varchar(100),
#                             brand varchar(100),
#                             model_num varchar (100),
#                             colors text,
#                             size varchar (50),
#                             name varchar(100),
#                             obj_condition varchar(100),
#                             orig_value float DEFAULT 0,
#                             purchase_price float DEFAULT 0,
#                             selling_price float DEFAULT 0,
#                             shipping_price float DEFAULT 0,
#                             uploaded varchar(10) DEFAULT "False",
#                             uploaded_to text,
#                             sold varchar(10) DEFAULT "False",
#                             imgfiles text,
#                             upldate datetime DEFAULT CURRENT_TIMESTAMP()
#                             )""")

#         if tablename.lower () == 'sales':
#             statement = (f"""CREATE TABLE {tablename}
#                             (_id varchar(30) PRIMARY KEY,
#                             item_id varchar(30),
#                             purchase_price float,
#                             selling_price float,
#                             shipping_price float,
#                             uploaded_to text,
#                             site_sold varchar(100),
#                             upldate datetime DEFAULT CURRENT_TIMESTAMP(),
#                             FOREIGN KEY (item_id) REFERENCES inventory(_id)
#                             ON UPDATE CASCADE
#                             )""")

    

#         if tablename.lower () == 'toys':
#             statement = (f"""CREATE TABLE {tablename}
#                             (_id varchar(30) PRIMARY KEY,
#                             item_id varchar(30),
#                             site_sold varchar(100),
#                             sold_price float,
#                             imgfile char(50),
#                             upldate datetime DEFAULT CURRENT_TIMESTAMP()
#                             )""")
        
#         if tablename.lower () == 'electronics':
#             statement = (f"""CREATE TABLE {tablename}
#                             (_id varchar(30) PRIMARY KEY,
#                             item_id varchar(30),
#                             site_sold varchar(100),
#                             sold_price float,
#                             imgfile char(50),
#                             upldate datetime DEFAULT CURRENT_TIMESTAMP()
#                             )""")

#         if tablename.lower () == 'clothes':
#             statement = (f"""CREATE TABLE {tablename}
#                             (_id varchar(30) PRIMARY KEY,
#                             item_id varchar(30),
#                             site_sold varchar(100),
#                             sold_price float,
#                             imgfile char(50),
#                             upldate datetime DEFAULT CURRENT_TIMESTAMP()
#                             )""")
            
#             # statement = (f"""CREATE TABLE {tablename}
#             #                 (_id varchar(30) PRIMARY KEY,
#             #                 category varchar(100),
#             #                 c_type varchar(100),
#             #                 brand varchar(100),
#             #                 name varchar(100),
#             #                 condition varchar(100),
#             #                 purchase_price money,
#             #                 selling_price money,
#             #                 uploaded bit DEFAULT 0, 
#             #                 sold bit DEFAULT 0,
#             #                 photo_paths text,
#             #                 upldate datetime DEFAULT CURRENT_TIMESTAMP()
#             #                 )""")

#         cur = self.connection.cursor ()
#         cur.execute(statement)
#         self.connection.commit()
#         print (f"Successfully added table {tablename}")


#     def run (self):
#         try:    
#             self.__createtable ('inventory')
#             self.__createtable ('sales')
#         except:
#             pass


# if __name__=='__main__':
#     db = DB()
#     db.run()
    
#     pass