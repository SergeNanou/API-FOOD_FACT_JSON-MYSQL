import mysql.connector

from general_variable import *
from category import *
from product import *
from cat_prod import *
from shop import *
from shop_prod import *
from substitut import *

# Creating the interface object with the database:
bd = GestionBD(GestionBD.host, GestionBD.database,
               GestionBD.user, GestionBD.password, GestionBD.charset)
if bd.echec:
    sys.exit()

# class instance
category = Category(bd, "category")
product = Product(bd, "product")
cat_prod = Cat_prod(bd, "Category_product")
shop_prod = Shop_prod(bd, "shop_product")
shop = Shop(bd, "shop")
substitut = Substitut(bd, "Substitut")
# Database tables create
category.create()
product.create()
cat_prod.create()
shop_prod.create()
substitut.create()
# call of data insert method
category.insert()
product.insert()
shop.insert()
cat_prod.insert()
shop_prod.insert()
