# coding: utf-8

import requests
import regex as re 
import unicodedata
class Product:
	"""This class represent the product table  in BDD"""
	def __init__(self, bd, table):
		
		self.bd = bd
		self.table = table
	# Method to create a Product table
	def create(self):
		statement =  ['CREATE TABLE IF NOT EXISTS %s \
                      (code_bar BIGINT  PRIMARY KEY,name_product TEXT,\
                      description TEXT,url  TEXT,nutrition_score CHAR(10))']
		for sql_insert_query in statement:
			if len(statement) > 0:
				self.bd.cursor.execute(sql_insert_query%(self.table))
	
	# Class Method to insert a data in Product tables
	def insert(self):
		# category types
		search = ['pizza', 'viennoiseries', 'Snacks', 'Epicerie', 'Desserts']
		# Openfoodfacts API request to take a data for category types
		for search_term in search:
		
			payload = {"search_terms": search_term,"search_tag": 
                       "categories","page_size": 1000, "json": 1}
			res = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?", 
                               params=payload)
			# url result 
			res.url
			liste_store = []
			# result of json request 
			results = res.json()
			products = results["products"]
			# selection data  type 
			for product in products:
				# test to ensure the our attributs presence 
				if 'nutrition_grade_fr' in product.keys() and  'product_name_fr' in product.keys() and  'stores' in product.keys() :
					if 'url' in product.keys() and 'code' in product.keys() and 'ingredients_text_fr' in product.keys() and  'stores' in product.keys():
						code = product['code']
						nutri = product['nutrition_grade_fr']
						prod = product['product_name_fr']
						# regex to delete punctuation in data
						prod =  re.sub(r"\p{P}+", r"", prod) 
						url = product['url']
						ingred = product['ingredients_text_fr']
						ingred = re.sub(r"\p{P}+", r"", ingred)
						store = product['stores']
						if code != '' and nutri != '' and prod != '' and url != '' and ingred != '' and store != '':
							# request to insert data recovered in product table 
							sql_insert_query = """ REPLACE  INTO Product \
                                               (code_bar, name_product, description, \
                                               url, nutrition_score) VALUES \
                                               ('%s', '%s','%s','%s','%s') """ %(code,prod,ingred,url, nutri)
							result  = self.bd.cursor.execute(sql_insert_query)
				
   
			#print (self.bd.cursor.rowcount, "Record inserted successfully into product table")