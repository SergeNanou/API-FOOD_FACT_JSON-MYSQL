# modules Import

import regex as re
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
# Openning database connect
bd_1 = mysql.connector.connect(host='localhost', database='Pure_beure',
                                user='root', password='', use_unicode=True, charset='utf8')
# cursor create
cursor = bd_1.cursor(buffered=True)
# class instance
category = Category(bd, "category")
product = Product(bd, "product")
cat_prod = Cat_prod(bd, "Category_product")
shop_prod = Shop_prod(bd, "shop_product")
shop = Shop(bd, "shop")
Substitut = Substitut(bd, "Substitut")
# Database tables create
category.create()
product.create()
cat_prod.create()
shop_prod.create()
# call of data insert method
category.insert()
product.insert()
shop.insert()
cat_prod.insert()
shop_prod.insert()

# Interact with user of application
myresult = []
myresult_1 = []
print("\n Entrer le numero de la categorie d'aliments à substituer  :\n"\
"1) Viennoiseries\n"\
"2) Snacks\n"\
"3) Epiceries\n"\
"4) Desserts\n"\
"5) Pizza\n")
# process to catch a user category choice
while True:
    ch = input('Valeur comprise entre 1 et 5:')
    try:
        ch = int(ch)
    except ValueError:
        print('Entrez un numero valide, SVP')
        continue
    if 1 <= ch <= 5:
        break
    else:
        print('Amplitude valide, SVP: 0 -', 5)

sc = ''
a = 0
if ch == 1:
    sc = 'viennoiseries'
    a = 1
if ch == 2:
    sc = 'Snacks'
    a = 2
if ch == 3:
    sc = 'Epicerie'
    a = 3
if ch == 4:
    sc = 'Desserts'
    a = 4
if ch == 5:
    sc = 'Pizza'
    a = 5
myresult = []

# process to catch a user  product number presentation choice
print("\n Entrer le nombre  de produits de cette categorie d'aliments que vous souhaiterez voir  :\n ")
while True:
    ch_1 = input('Valeur comprise entre 1 et 10:')
    try:
        ch_1 = int(ch_1)
    except ValueError:
        print('Entrez un numero valide , SVP')
        continue
    if 1 <= ch_1 <= 10:
        break
    else:
        print('Amplitude valide, SVP: 1 -', 10)

if ch == a:
    # request in database to take a same category  product of user choice
    display_product = "SELECT DISTINCT p.name_product FROM Product AS P  WHERE (p.code_bar IN (SELECT cp.product_code_bar FROM Category_product AS cp WHERE cp.categorie_id IN(SELECT c.id FROM category AS C WHERE c.name_category = %s))) "
    # request execute
    bd.cursor.execute(display_product, (sc, ))
    # request result
    myresult = bd.cursor.fetchmany(ch_1)
    # show result request to user
    for x in range(len(myresult)):
        print(x+1, ':', myresult[x][0])
# process to catch a user product choice
print("\n Entrer le numero du produit à substituer  :\n")
while True:
    ch_2 = input('Valeur comprise entre 1 et le nombre de produits choisis:')
    try:
        ch_2 = int(ch_2)
    except ValueError:
        print('Entrez un numero valide , SVP')
        continue
    if 1 <= ch_2 <= len(myresult):
        break
    else:
        print('Amplitude valide, SVP: 0 -', len(myresult))
# process to catch a user  substitut number presentation choice
choice_prod = myresult[ch_2-1][0]
print("\n Entrer le nombre  d'aliments substituts plus riche  :\n")
while True:
    ch_3 = input('Valeur comprise entre 1 et 5:')
    try:
        ch_3 = int(ch_3)
    except ValueError:
        print('Entrez un numero valide, SVP')
        continue
    if 1 <= ch_3 <= 5:
        break
    else:
        print('Amplitude valide, SVP: 0 -', 5)

sc_1 = 'a'
# request to take the name, the composition and the shop of substitut product
display_subs = "SELECT p.name_product, p.description, p.url,s.name_shop FROM Product p LEFT JOIN  Category_product AS cp  ON  p.code_bar = cp.product_code_bar LEFT JOIN Category AS C ON c.id = cp.categorie_id LEFT JOIN  shop_product AS sp  ON  p.code_bar  =  sp.product_code_bar LEFT JOIN Shop AS s ON sp.shop_id = s.id  WHERE c.name_category = %s and  p.nutrition_score = %s"
# request execute
bd.cursor.execute(display_subs, (sc, sc_1, ))
# request result
myresult_1 = bd.cursor.fetchmany(ch_3)
for x in range(len(myresult_1)):
    # request result showing
    print(x+1, '-', '\n nom du produit: {}'\
        '\n composition du produit: {}'\
        '\n lien url openfoodfacts  du produit: {}'\
        '\n Supermarché vendant le produit: {}'.format(myresult_1[x][0],
         myresult_1[x][1], myresult_1[x][2], myresult_1[x][3]))
# process to catch a user  saving substitut choice 
print("\n Voulez-vous enregistrez le produit et son substitut plus riche  :\n"\
"1) Oui\n"\
"2) Non\n")
while True:
    ch_4 = input('Votre choix entre 1 ou 2:')
    try:
        ch_4 = int(ch_4)
    except ValueError:
        print('Entrez un numero valide , SVP')
        continue
    if  ch_4 == 2:
        print("Vous avez souhaité ne pas enregistré votre produit de substitution\n" \
            "Merci de votre visite.A bientot")
        break
    elif ch_4 == 1:
        
        # Variables init
        s = 'Substitut'
        result_final = []
        s_b = myresult[ch_2-1][0]
        s_1 = str(re.sub(r"\p{P}+", r"", s_b))
        s_a = myresult_1[0][0]
        s_2 = str(re.sub(r"\p{P}+", r"", s_a))
        
        statement_1 = """REPLACE INTO Substitut(name_product, product_substitut) VALUES (%s,%s)"""
        bd.cursor.execute(statement_1, (s_1, s_2))
        print("le produit et son substitut ont été correctement enregistré \n"\
            "Merci de votre visite")
        break
    else:
        print('choix valide, SVP: 1 ou ', 2)
# Database Connection closing and save operate transform
bd.baseDonn.commit()
bd.cursor.close()
bd.baseDonn.close()
