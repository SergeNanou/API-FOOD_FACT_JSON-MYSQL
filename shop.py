from main import *


class Shop:
	def __init__(self, bd, table):
		
		self.bd = bd
		self.table = table
	def create(self):
		statement =  ['DROP TABLE IF EXISTS %s','CREATE TABLE %s (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT  PRIMARY KEY,name_shop VARCHAR(100) NOT NULL)']
		
		for sql_insert_query in statement:
			if len(statement) > 0:
				self.bd.cursor.execute(sql_insert_query%(self.table))
	
	def insert(self):
		records_to_insert = []
		for elt in enumerate(liste_store):
			records_to_insert.append(elt)

		
		sql_insert_query = """ INSERT INTO Shop (id, name_shop) VALUES (%s,%s) """
		
   		#used executemany to insert 3 rows
		result  = self.bd.cursor.executemany(sql_insert_query, records_to_insert)
   
		print (self.bd.cursor.rowcount, "Record inserted successfully into category table")