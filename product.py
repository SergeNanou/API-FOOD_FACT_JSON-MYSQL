# coding: utf-8

import requests
import regex as re 
import unicodedata
class Product:
	"""This class represent the produit table  in BDD"""
	def __init__(self, bd, table):
		
		self.bd = bd
		self.table = table
	def create(self):
		statement =  ['DROP TABLE IF EXISTS %s','CREATE TABLE %s (code_bar BIGINT  PRIMARY KEY,name_product TEXT,description TEXT,url  TEXT,nutrition_score CHAR(10))']
		
		for sql_insert_query in statement:
			if len(statement) > 0:
				self.bd.cursor.execute(sql_insert_query%(self.table))
	# def insert(self):
	# 	for product in products:
	# 		if product[]
	def insert(self):

		search = ['pizza', 'Boissons', 'Snacks', 'Epicerie', 'Desserts','pizza']
		for search_term in search:
		
			payload = {"search_terms": search_term,"search_tag": "categories","page_size": 1000, "json": 1}
			res = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?", params=payload)

			# l'url correspondante
			res.url
			liste_store = []
			# on peut ensuite récupérer les produits
			results = res.json()
			products = results["products"]
			for product in products:
				if 'nutrition_grade_fr' in product.keys() and  'product_name_fr' in product.keys() and  'stores' in product.keys():
					if 'url' in product.keys() and 'code' in product.keys() and 'ingredients_text_fr' in product.keys():
						code = product['code']
						nutri = product['nutrition_grade_fr']
						prod = product['product_name_fr']
						#prod = unicode(prod,'utf-8')
						prod =  re.sub(r"\p{P}+", r"", prod)
					

						#prod = re.sub(r"\p{P}+", r"", prod)
						url = product['url']
						ingred = product['ingredients_text_fr']
						ingred = re.sub(r"\p{P}+", r"", ingred)
						sql_insert_query = """ REPLACE  INTO Product (code_bar, name_product, description, url, nutrition_score) VALUES ('%s', '%s','%s','%s','%s') """ %(code,prod,ingred,url, nutri)
						result  = self.bd.cursor.execute(sql_insert_query)
				#print(nutri)
   
			print (self.bd.cursor.rowcount, "Record inserted successfully into product table")