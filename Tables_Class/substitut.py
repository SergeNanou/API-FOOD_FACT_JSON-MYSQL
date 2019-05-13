
class Substitut:
	"""This class represent the substitut table  in BDD"""
	def __init__(self, bd, table):
		
		self.bd = bd
		self.table = table
	# Method to create a Substitut table
	def create(self):

		statement =  ['DROP TABLE IF EXISTS %s',
		              'CREATE TABLE IF NOT EXISTS %s \
		              (id SMALLINT  UNSIGNED AUTO_INCREMENT PRIMARY KEY,\
		              name_product TEXT NOT NULL, composition TEXT NOT NULL,\
		              url TEXT NOT NULL, name_shop VARCHAR(100) NOT NULL,\
		              product_substitut TEXT NOT NULL)']
		
		#self.bd.cursor.execute(statement[0]%(self.table))
		self.bd.cursor.execute(statement[1]%(self.table))
	