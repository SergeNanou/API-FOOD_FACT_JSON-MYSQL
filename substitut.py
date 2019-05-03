
class Substitut:
	"""This class represent the substitut table  in BDD"""
	def __init__(self, bd, table):
		
		self.bd = bd
		self.table = table
	def create(self):
		statement =  ['DROP TABLE IF EXISTS %s','CREATE TABLE %s (id SMALLINT  UNSIGNED AUTO_INCREMENT PRIMARY KEY,name_produit VARCHAR(100) NOT NULL,product_substitut VARCHAR(100) NOT NULL)']
		
		for sql_insert_query in statement:
			if len(statement) > 0:
				self.bd.cursor.execute(sql_insert_query%(self.table))
	