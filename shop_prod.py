from shop_1 import *

class Shop_prod:
	"""This class represent the shop_product table  in BDD"""
	def __init__(self, bd, table):
		
		self.bd = bd
		self.table = table
	#Class method to create shop_ptroduct table
	def create(self):
		statement =  ['DROP TABLE IF EXISTS %s','CREATE TABLE %s (shop_id SMALLINT   REFERENCES Shop(id),product_code_bar BIGINT REFERENCES Product(code_bar),PRIMARY KEY (shop_id, product_code_bar))']
		
		for sql_insert_query in statement:
			if len(statement) > 0:
				self.bd.cursor.execute(sql_insert_query%(self.table))
	# Class Method to insert a data in Shop Product tables
	def insert(self):
		# Category types
		search = ['Viennoiseries', 'Snacks', 'Epicerie', 'Desserts','pizza']
		records_to_insert = []
		for elt in enumerate(liste_store):
			records_to_insert.append(elt)

		for search_term in search:
			# Openfoodfacts API request to take a data for category types
			payload = {"search_terms": search_term,"search_tag": "categories","page_size": 1000, "json": 1}
			res = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?", params=payload)
			# url result 
			res.url
			# # result of json request 
			results = res.json()
			products = results["products"]
			for product in products:
				# test to ensure the our attributs presence 
				if 'nutrition_grade_fr' in product.keys() and  'product_name_fr' in product.keys() and 'stores' in product.keys():
					if 'url' in product.keys() and 'code' in product.keys() and 'ingredients_text_fr' in product.keys():
						# Selection result
						code = product['code']
						store = product['stores']
						id_store = 0

						for record in records_to_insert:
							if store in record[1]:
								id_store = record[0]
						# request to insert data recovered in shop_product table 
						sql_insert_query = """ REPLACE INTO Shop_product (shop_id, product_code_bar) VALUES (%s, %s) """ %(id_store,code)
						result  = self.bd.cursor.execute(sql_insert_query)
				
			print (self.bd.cursor.rowcount, "Record inserted successfully into shop_prod table")
	