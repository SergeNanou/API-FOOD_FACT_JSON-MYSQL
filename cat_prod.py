import requests
from general_variable import *
import mysql.connector
from mysql.connector import Error
class Cat_prod:
	"""This class represent the category_product table  in BDD"""
	def __init__(self, bd, table):
		
		self.bd = bd
		self.table = table
	# Method to create a Product table
	def create(self):
		statement =  ['DROP TABLE IF EXISTS %s','CREATE TABLE %s (categorie_id SMALLINT   REFERENCES Category(id),product_code_bar BIGINT  REFERENCES Product(code_bar),PRIMARY KEY (categorie_id, product_code_bar))']
		
		for sql_insert_query in statement:
			if len(statement) > 0:
				self.bd.cursor.execute(sql_insert_query%(self.table))
	# Class Method to insert a data in cat_Prod tables
	def insert(self):
		# type of category
		search = ['Viennoiseries', 'Snacks', 'Epicerie', 'Desserts','pizza']
		for search_term in search:

			if search_term == 'Viennoiseries':
				cat = 1
			if search_term == 'Snacks':
				cat = 2
			if search_term == 'Epicerie':
				cat = 3
			if search_term == 'Desserts':
				cat = 4
			if search_term == 'pizza':
				cat = 5
			# Openfoodfacts API request to take a data for category types
			payload = {"search_terms": search_term,"search_tag": "categories","page_size": 1000, "json": 1}
			res = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?", params=payload)

			# # url result 
			res.url
			liste_store = []
			# result of json request 
			results = res.json()
			products = results["products"]
			# selection data  type
			for product in products:
				# test to ensure the our attributs presence 
				if 'nutrition_grade_fr' in product.keys() and  'product_name_fr' in product.keys() and 'stores' in product.keys():
					if 'url' in product.keys() and 'code' in product.keys() and 'ingredients_text_fr' in product.keys():
						code = product['code']
						# request to insert data recovered in category_product table 
						sql_insert_query = """ REPLACE INTO Category_product (categorie_id, product_code_bar) VALUES (%s, %s) """ %(cat,code)
						result  = self.bd.cursor.execute(sql_insert_query)
				#print(code, cat)
   
			print (self.bd.cursor.rowcount, "Record inserted successfully into cat_prod table")