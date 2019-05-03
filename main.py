import requests

payload = {"search_terms": "pizza","search_tag": "categories","page_size": 200, "json": 1}
res = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?", params=payload)

# l'url correspondante
res.url
liste_store = []
# on peut ensuite récupérer les produits
results = res.json()
products = results["products"]
#stores = results["stores"]
#print(len(products))
#print(products[0]["ingredients_text_fr"])
# Et afficher leurs noms
for product in products:
    #print(product.keys())
    #print(product['url'])
    if 'stores' in product.keys():
    	liste_store.append(product['stores'])

liste_coma = []
coma = ","
for store in liste_store:
	if coma in store:
		liste_coma.append(store)
		
#print(liste_store)
for element in liste_coma:
	b = element.split(",")
	for a in b:

		liste_store.append(a)
#liste_store = list(set(liste_store))
#print(liste_store)
for c in liste_coma:
	
	liste_store.remove(c)
liste_store = list(set(liste_store))
liste_store.remove('')
#print(liste_store)
records_to_insert = []
for elt in enumerate(liste_store):
	records_to_insert.append(elt)

#print(records_to_insert)