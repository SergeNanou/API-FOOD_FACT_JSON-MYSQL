from general_variable import *
from category import *
from product import *
from cat_prod import *
from substitut import *
from shop import *
from shop_prod import *



# Création de l'objet-interface avec la base de données : 
bd = GestionBD(GestionBD.host, GestionBD.database, GestionBD.user, GestionBD.password, GestionBD.charset)
if bd.echec:
	sys.exit()

category = Category(bd,"category")
product = Product(bd, "product")
cat_prod = Cat_prod(bd, "Category_product")
substitut = Substitut(bd, "substitut")
shop_prod = Shop_prod(bd, "shop_product")
shop = Shop(bd, "shop")
category.create()
product.create()
cat_prod.create()
substitut.create()
shop_prod.create()
category.insert()
product.insert()
shop.insert()
cat_prod.insert()
shop_prod.insert()
#cursor= bd.cursor()
#table_name_drop = [categor, categorie_product, categorie_produit, cato, magasin, produit, produit_magasin]

#bd.cursor.execute("DROP TABLES produit_magasin") 
bd.cursor.execute("SELECT * FROM shop_product")
myresult =bd.cursor.fetchall()

cpt = 0
for x in myresult:
	
  print(x)
print(len(myresult))
#for (table_name,) in bd.cursor:
       # print(table_name)