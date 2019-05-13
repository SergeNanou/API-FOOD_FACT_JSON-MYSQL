# Import modules

from general_variable import *
import mysql.connector
from mysql.connector import Error


class Category:
    """This class represent the category table in BDD"""
    def __init__(self, bd, table):

        self.bd = bd
        self.table = table
    # Method to create a category table
    def create(self):

        statement = ['CREATE TABLE  IF NOT EXISTS %s \
                    (id SMALLINT  UNSIGNED NOT NULL \
                    AUTO_INCREMENT  PRIMARY KEY,\
                    name_category VARCHAR(255) NOT NULL)']

        for sql_insert_query in statement:
            if len(statement) > 0:
                # request execute
                self.bd.cursor.execute(sql_insert_query % (self.table))
    # Method to insert a data in category table
    def insert(self):

        records_to_insert = [(1, 'Viennoiseries'), (2, 'Snacks'),
                             (3, 'Epicerie'), (4, 'Desserts'),
                             (5, 'pizza')]
        sql_insert_query = """ REPLACE INTO Category\
                               (id, name_category) VALUES (%s, %s) """
        # used executemany to insert 3 rows
        result = self.bd.cursor.executemany(sql_insert_query,
                                            records_to_insert)
