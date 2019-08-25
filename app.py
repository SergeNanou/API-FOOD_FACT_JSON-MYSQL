
import regex as re
import mysql.connector

from general_variable import *


def exec_mysql_1(display_product,ch_s):     
    # Creating the interface object with the database:
    bd = GestionBD(GestionBD.host, GestionBD.database,
                   GestionBD.user, GestionBD.password, GestionBD.charset)
    if bd.echec:
        sys.exit()
    
    
    # request execute
    bd.cursor.execute(display_product, (ch_s, ))
    bd.baseDonn.commit()
    bd.cursor.close()
    bd.baseDonn.close()

def run_q_1():
    display_product = 'SELECT DISTINCT p.name_product \
                       FROM Product AS P  WHERE(p.code_bar IN \
                       (SELECT cp.product_code_b FROM Category_product \
                       AS cp WHERE cp.categorie_id IN(SELECT c.id FROM \
                       category AS C WHERE c.name_category = %s))) \
                       ORDER BY RAND()'
    ch_s = 'Pizza'
    exec_mysql_1(display_product,ch_s)

def exec_mysql_2(ch_s, sc_1, display_subs):     
    # Creating the interface object with the database:
    bd = GestionBD(GestionBD.host, GestionBD.database,
                   GestionBD.user, GestionBD.password, GestionBD.charset)
    if bd.echec:
        sys.exit()
    
    
    # request execute
    bd.cursor.execute(display_subs, (ch_s,sc_1, ))
    bd.baseDonn.commit()
    bd.cursor.close()
    bd.baseDonn.close()

def run_q_2():
    display_subs = 'SELECT p.name_product, p.description, p.url,s.name_shop \
                                   FROM Product p LEFT JOIN  Category_product AS cp ON  \
                                   p.code_bar = cp.product_code_bar LEFT JOIN Category AS C ON\
                                   c.id = cp.categorie_id LEFT JOIN  shop_product AS sp  ON\
                                   p.code_bar  =  sp.product_code_bar LEFT JOIN Shop AS s ON\
                                   sp.shop_id = s.id  WHERE c.name_category = %s and\
                                   p.nutrition_score = %s ORDER BY RAND()'
    ch_s = 'Pizza'
    sc_1 = 'a'
    exec_mysql_2(display_subs, (ch_s,sc_1, ))

def exec_mysql_3(ch_s, statement_1, s_1, s_3, s_4, s_5,s_2):     
    # Creating the interface object with the database:
    bd = GestionBD(GestionBD.host, GestionBD.database,
                   GestionBD.user, GestionBD.password, GestionBD.charset)
    if bd.echec:
        sys.exit()
    
    
    # request execute
    bd.cursor.execute(statement_1, (s_1, s_3, s_4,s_2,ch_s))
    bd.baseDonn.commit()
    bd.cursor.close()
    bd.baseDonn.close()

def run_q_3():
    statement_1 = "REPLACE INTO Substitut(name_product, composition, url, product_substitut, category) VALUES (%s, %s, %s, %s, %s, %s)"
    ch_s = 'Pizza'
    s_1 = 'La Crazy'
    s_2 = 'Bases Pizza'
    s_3 = 'Farine de blé contient Gluten avec de carbonate de calcium Fer Niacine Thiamine  Eau  Semoule de blé dur contient  Huile dolive vierge extra 0  Levure  Huile de colza  Vinaigre  Farine de blé fermenté déshydrate contient Gluten  Poudre à lever  E450 Bicarbonate soude Phosphate de calcium  Sel  Lait en poudre écrémé'
    s_4 = 'lien: https://fr.openfoodfacts.org/produit/00790956/bases-pizza-marks-spencer'

    exec_mysql_3(statement_1, (s_1, s_3, s_4, s_2,ch_s))
            
            

# def test(event):
#     sub= ()
#     sub = choice_prod.curselection()
#     sub_0 = sub[0]
#     canvas = Canvas(master, width=270, height=50)
#     canvas['bg']='green'
#     canvas.text = canvas.create_text(110, 30, text=my_result[sub_0][0])
#     canvas.place(x=270, y=230)  
#     sc_1 = 'a'
#     # request to take the name,
#     # the composition and the shop of substitut product
#     bd = GestionBD(GestionBD.host, GestionBD.database,
#                    GestionBD.user, GestionBD.password, GestionBD.charset)
#     if bd.echec:
#         sys.exit()
#     display_subs = "SELECT p.name_product, p.description, \
#                     p.url,s.name_shop FROM Product p \
#                     LEFT JOIN  Category_product AS cp  \
#                     ON  p.code_bar = cp.product_code_bar \
#                     LEFT JOIN Category AS C ON c.id = cp.categorie_id \
#                     LEFT JOIN  shop_product AS sp  ON  \
#                     p.code_bar  =  sp.product_code_bar \
#                     LEFT JOIN Shop AS s ON \
#                     sp.shop_id = s.id  \
#                     WHERE c.name_category = %s \
#                     and  p.nutrition_score = %s \
#                     ORDER BY RAND()"
#     # request execute
#     bd.cursor.execute(display_subs, (ch_s, sc_1, ))
#     # request result
#     myresult_1 = bd.cursor.fetchmany(1)
                    
#     choice_prod_1 = Text(root, width=45,height=10)
#     choice_prod_1['bg']='ivory'
#     choice_prod_1.place(x=250, y=310)
                   
#     choice_prod_1.insert('1.0','nom: '+ myresult_1[0][0]+'\n')
#     choice_prod_1.insert('2.0','composition: '+ myresult_1[0][1]+'\n')
#     choice_prod_1.insert('3.0','lien: '+ myresult_1[0][2]+'\n')
#     s_5 = myresult_1[0][3]
#     if myresult_1[0][3] == None:
#         s_5 = ''
#     choice_prod_1.insert('4.0','Shop: '+ s_5)
                    
                        
#     var_ch_1 = IntVar()
# def cb():
                        
#     if var_ch_1.get()==1:
#         s_1 = my_result[sub_0][0]
#         s_2 = myresult_1[0][0]
#         s_3 = myresult_1[0][1]
#         s_4 = myresult_1[0][2]
#         if myresult_1[0][3] == None:
#             s_5 = ''
#         else: 
#         s_5 = myresult_1[0][3]
                                
#     statement_1 = "REPLACE INTO Substitut\
#                    (name_product, composition, url, name_shop, \
#                     product_substitut, category) \
#                     VALUES (%s, %s, %s, %s, %s, %s)"
#     bd.cursor.execute(statement_1, (s_1, s_3, s_4, s_5,s_2,ch_s))
#     showinfo("Alerte", "VOTRE ALIMENT ET SON SUBSTITUT  SONT ENREGISTRES")
                    
#     choice_save = ttk.Checkbutton(master, text="Enregistrez le produit et substitut",
#                                   variable=var_ch_1,onvalue = 1, offvalue = 0, command=cb)
#     choice_save.place(x=330, y=480)
#     choice_prod.bind("<<ListboxSelect>>", test)

                    
#         break
#     else:
#         showinfo("Alerte", "CHOISISSEZ UNE CATEGORIE SVP")
#         break

#     bd.baseDonn.commit()
#     bd.cursor.close()
#     bd.baseDonn.close()