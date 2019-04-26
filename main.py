import requests

payload = {"search_terms": "pizza","search_tag": "categories","page_size": 1, "json": 1}
res = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?", params=payload)

# l'url correspondante
res.url

# on peut ensuite récupérer les produits
results = res.json()
products = results["products"]
#stores = results["stores"]
print(len(products))
#print(products[0]["ingredients_text_fr"])
# Et afficher leurs noms
for product in products:
    #print(product.keys())
    print(product["product_name"])

