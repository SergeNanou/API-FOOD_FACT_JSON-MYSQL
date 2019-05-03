import requests

payload = {"search_terms": "pizza","search_tag": "categories","page_size": 1, "json": 1}
res = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?", params=payload)

# l'url correspondante
res.url
liste_store = []
# on peut ensuite récupérer les produits
results = res.json()
products = results["products"]
#stores = results["stores"]
print(len(products))
#print(products[0]["ingredients_text_fr"])
# Et afficher leurs noms
#for product in products:
    #print(product.keys())
    #print(product['categories'])
for product in products:
	if 'nutrition_grade_fr' in product.keys() and  'product_name_fr' in product.keys():
		if 'url' in product.keys() and 'code' in product.keys() and 'ingredients_text_fr' in product.keys():
			code = product['code']
			nutri = product['nutrition_grade_fr']
			prod = product['product_name_fr']
			url = product['url']
			ingred = product['ingredients_text_fr']
			sql_insert_query = """ INSERT INTO Product (code_bar, name_product,description,url, nutrition_score) VALUES (%s,%s,%s, %s,%s) """ %(code, prod, ingred,url,nutri)
			#result  = self.bd.cursor.execute(sql_insert_query)
		print(code,nutri, prod, url,ingred)