# modules Import
import random
import regex as re
import mysql.connector

from general_variable import *

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import sys

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Pure Beurre appli pour le choix d'aliments saints")
        master['bg']='orange'
        master.geometry('%dx%d+%d+%d' % (1070, 600,150,50))
        # structure  interface create
        self.Frame1 = Frame(master, borderwidth=2, relief=GROOVE)
        self.Frame1.pack(side=TOP  ,padx=10, pady=10)
        self.Frame2 = Frame(master, borderwidth=2, relief=GROOVE).place(x=270, y=200)
        Label(self.Frame2, text="PRODUITS CHOISIS ET  SUBSTITUT ENREGISTRES ").place(x=270, y=200)
        Label(self.Frame1, text="CHOIX DES CATEGORIES DE PRODUITS")\
        .pack(padx=10, pady=10)
        self.Frame3 = Frame(master, borderwidth=2, relief=GROOVE).place(x=320, y=290)
        Label(self.Frame3, text="SUBSTITUTS ").place(x=320, y=290)

    
        self.var_ch = ''
        # list choices buildings
        self.var_ch = StringVar()


        self.choice_Vien = Radiobutton(master, text="Viennoiseries",
                                      variable=self.var_ch, value="Viennoiseries")
        self.choice_Sna = Radiobutton(master, text="Snacks",
                                      variable=self.var_ch, value="Snacks")
        self.choice_Epic = Radiobutton(master, text="Epiceries",
                                       variable=self.var_ch, value="Epicerie")
        self.choice_Des = Radiobutton(master, text="Desserts",
                                      variable=self.var_ch, value="Desserts")
        self.choice_Piz = Radiobutton(master, text="Pizza",
                                      variable=self.var_ch, value="Pizza")


        self.choice_Vien.pack()
        self.choice_Sna.pack()
        self.choice_Epic.pack()
        self.choice_Des.pack()
        self.choice_Piz.pack()
        def recupere():
            self.my_result = []
            self.my_result_1 = []
            

            
            # Creating the interface object with the database:
            bd = GestionBD(GestionBD.host, GestionBD.database,
                           GestionBD.user, GestionBD.password, GestionBD.charset)
            if bd.echec:
                sys.exit()
            while True:
                self.ch_s = self.var_ch.get()
                
                if self.ch_s != '':
                    self.display_product = "SELECT DISTINCT p.name_product \
                                       FROM Product AS P  WHERE\
                                       (p.code_bar IN (SELECT cp.product_code_bar \
                                       FROM Category_product\
                                       AS cp WHERE cp.categorie_id \
                                       IN(SELECT c.id FROM category AS C \
                                       WHERE c.name_category = %s)))\
                                       ORDER BY RAND() "
                    # request execute
                    bd.cursor.execute(self.display_product, (self.ch_s, ))
                    # request result
                    self.my_result = bd.cursor.fetchmany(10)  
                    self.choice_prod = Listbox(master, width=40)
                    self.choice_prod.place(x=0, y=250)
                    print(self.choice_prod['listvariable'])
                    for a in range(len(self.my_result)):
                        
                        self.choice_prod.insert(a+1, self.my_result[a][0])
                    #function to display selection
                    def test(event):
                        self.s_5 = ''
                        self.s_6 = ''
                        self.sub= ()
                        self.sub = self.choice_prod.curselection()
                        self.sub_0 = self.sub[0]
                    
                        self.canvas = Canvas(master, width=270, height=50)
                        self.canvas['bg']='green'
                        self.canvas.text = self.canvas.create_text(110, 
                                           30, text=self.my_result[self.sub_0][0])
                        self.canvas.place(x=270, y=230)  
                        sc_1 = 'a'
                        s_c_1 = 'b'
                        # request to take the name,
                        # the composition and the shop of substitut product
                        bd = GestionBD(GestionBD.host, GestionBD.database,
                                  GestionBD.user, GestionBD.password, GestionBD.charset)
                        if bd.echec:
                            sys.exit()
                        self.nut = "SELECT p.nutrition_score FROM \
                                    Product p WHERE p.name_product=%s"

                        bd.cursor.execute(self.nut, (self.my_result[self.sub_0][0],))
                        self.res_nut = bd.cursor.fetchmany()
                        self.res_nut = self.res_nut[0][0]
                        self.myresult_1 = []
                        self.my_res = []
                        if (self.res_nut == 'c' or self.res_nut == 'd'
                            or self.res_nut == 'e'):

                            self.display_subs = "SELECT p.name_product, p.description, \
                                        p.url,s.name_shop FROM Product p \
                                        LEFT JOIN  Category_product AS cp  \
                                        ON  p.code_bar = cp.product_code_bar \
                                        LEFT JOIN Category AS C ON c.id = cp.categorie_id \
                                        LEFT JOIN  shop_product AS sp  ON  \
                                        p.code_bar  =  sp.product_code_bar \
                                        LEFT JOIN Shop AS s ON \
                                        sp.shop_id = s.id  \
                                        WHERE c.name_category = %s \
                                        and  p.nutrition_score = %s \
                                        ORDER BY RAND()"

                            # request execute
                            bd.cursor.execute(self.display_subs, (self.ch_s, sc_1, ))
                            # request result
                            if bd.cursor.fetchmany(1)==[]:

                                self.myresult_1 = bd.cursor.fetchmany(1)
                            else:
                                bd.cursor.execute(self.display_subs, (self.ch_s, s_c_1, )) 
                                self.myresult_1 = bd.cursor.fetchmany(1)
                            
                            print(self.myresult_1)
                            # self.my_res = bd.cursor.fetchmany(1)
                            
                            # display result of selection
                            # algorithm of selection
                            self.choice_prod_1 = Text(root, width=45,height=10)
                            self.choice_prod_1['bg']='ivory'
                            self.choice_prod_1.place(x=250, y=310)
                            # self.defilY = Scrollbar(master, orient='vertical',
                            #                         command=self.choice_prod_1.yview)
                            # self.defilY.place(x=610, y=310, height=165)
                            
                            # self.choice_prod_1['yscrollcommand'] = self.defilY.set
                            self.choice_prod_1.insert('1.0','prod_score: '+ 
                                                      self.myresult_1[0][0]+'\n')
                            self.choice_prod_1.insert('2.0','composition: '+ 
                                                      self.myresult_1[0][1]+'\n')
                            self.choice_prod_1.insert('3.0','lien: '+ 
                                                      self.myresult_1[0][2]+'\n')
                            self.s_5 = ''
                            self.s_5 = self.myresult_1[0][3]
                            print(self.s_5)
                            if self.myresult_1[0][3] == None:
                                self.s_5 = ''
                            self.choice_prod_1.insert('4.0','Shop: '+ self.s_5 +'\n')
                            # self.choice_prod_1.insert('5.0',
                            #                 '================================='+'\n')
                            # self.choice_prod_1.insert('6.0','prod_score_b: '+ self.my_res[0][0]+'\n')
                            # self.choice_prod_1.insert('7.0','composition: '+ self.my_res[0][1]+'\n')
                            # self.choice_prod_1.insert('8.0','lien: '+ self.my_res[0][2]+'\n')
                            # self.s_6 = ''
                            # self.s_6 = self.my_res[0][3]
                            # print(self.s_6)
                            # if self.my_res[0][3] == None:
                            #     self.s_6 = ''
                            # self.choice_prod_1.insert('9.0','Shop: '+ self.s_6)
                            # print('Shop: '+ self.s_6)
                        else:
                            self.display_subs = "SELECT p.name_product, p.description, \
                                        p.url,s.name_shop FROM Product p \
                                        LEFT JOIN  Category_product AS cp  \
                                        ON  p.code_bar = cp.product_code_bar \
                                        LEFT JOIN Category AS C ON c.id = cp.categorie_id \
                                        LEFT JOIN  shop_product AS sp  ON  \
                                        p.code_bar  =  sp.product_code_bar \
                                        LEFT JOIN Shop AS s ON \
                                        sp.shop_id = s.id  \
                                        WHERE c.name_category = %s \
                                        and  p.nutrition_score = %s \
                                        ORDER BY RAND()"

                            # request execute
                            bd.cursor.execute(self.display_subs, (self.ch_s, sc_1, ))
                            # request result
                            self.myresult_1 = bd.cursor.fetchmany(1)

                            bd.cursor.execute(self.display_subs, (self.ch_s, s_c_1, ))
                            self.my_res = bd.cursor.fetchmany(1)

                            self.choice_prod_1 = Text(root, width=45,height=10)
                            self.choice_prod_1['bg']='ivory'
                            self.choice_prod_1.place(x=250, y=310)
                            
                            self.choice_prod_1.insert('1.0','prod_score_a: '+ self.myresult_1[0][0]+'\n')
                            self.choice_prod_1.insert('2.0','composition: '+ self.myresult_1[0][1]+'\n')
                            self.choice_prod_1.insert('3.0','lien: '+ self.myresult_1[0][2]+'\n')
                            
                            self.s_5 = ''
                            self.s_5 = self.myresult_1[0][3]

                            if self.myresult_1[0][3] == None:
                                self.s_5 = ''
                            self.choice_prod_1.insert('4.0','Shop: '+ self.s_5) 
                        self.var_ch_1 = IntVar()
                        def cb():
                        
                            if self.var_ch_1.get()==1:
                                self.s_1 = self.my_result[self.sub_0][0]
                                
                                self.s_2 = self.myresult_1[0][0]
                            
                                self.s_3 = self.myresult_1[0][1]
                                self.s_4 = self.myresult_1[0][2]
                            if self.myresult_1[0][3] == None:
                                self.s_5 = ''
                            else: 
                                self.s_5 = self.myresult_1[0][3]
                                
                            self.statement_1 = "REPLACE INTO Substitut\
                                          (name_product, composition, url, name_shop, \
                                          product_substitut, category) \
                                          VALUES (%s, %s, %s, %s, %s, %s)"
                            bd.cursor.execute(self.statement_1, 
                                             (self.s_1, self.s_3, 
                                             self.s_4, self.s_5,
                                             self.s_2,self.ch_s))

                            showinfo("Alerte", "VOTRE ALIMENT ET SON SUBSTITUT  SONT ENREGISTRES")
                    
                    
                        self.choice_save = ttk.Checkbutton(master, text="Enregistrez le produit et substitut",
                                    variable=self.var_ch_1,onvalue = 1, offvalue = 0, command=cb)
                        self.choice_save.place(x=330, y=480)
                    
                        

                    self.choice_prod.bind("<<ListboxSelect>>", test)

                    
                    break
                else:
                    showinfo("Alerte", "CHOISISSEZ UNE CATEGORIE SVP")
                break

            bd.baseDonn.commit()
            bd.cursor.close()
            bd.baseDonn.close()
        # function to display a product substitut
        def save():

            # Creating the interface object with the database:
            bd = GestionBD(GestionBD.host, GestionBD.database,
                           GestionBD.user, GestionBD.password, GestionBD.charset)
            if bd.echec:
                sys.exit()
            while True:
                self.ch_s = self.var_ch.get()
                
                if self.ch_s != '':
                    self.state_choice = "SELECT * FROM SUBSTITUT WHERE Category = %s"
                    bd.cursor.execute(self.state_choice, (self.ch_s, ))
                    self.result_one = bd.cursor.fetchall()

                    if self.result_one == []:
                        showinfo("Alerte", "Vous n'avez pas de favoris enregistrés pour cette categorie")
                        break
                    else:
                        self.choice_prod_2 = Text(master, width=45,height=10)

                        self.choice_prod_2.place(x=635, y=280)
                        self.defilY = Scrollbar(master, orient='vertical',
                            command=self.choice_prod_2.yview)
                        self.defilY.place(x=990, y=280, height=165)
        
                        self.choice_prod_2['yscrollcommand'] = self.defilY.set
                        for x in range(len(self.result_one)):
                            self.choice_prod_2.insert('1.0','aliment: '+ self.result_one[x][1]+'\n')
                            self.choice_prod_2.insert('2.0','substitut: '+ self.result_one[x][5]+'\n')
                            self.choice_prod_2.insert('3.0','description: '+ self.result_one[x][2]+'\n')
                            self.choice_prod_2.insert('4.0','lien: '+ self.result_one[x][3]+'\n')
                            self.choice_prod_2.insert('5.0','Shop: '+ self.result_one[x][4]+'\n')
                            self.choice_prod_2.insert('6.0', '================================================')
                            
                    break
                else:
                    showinfo("Alerte", "CHOISISSEZ UNE CATEGORIE SVP")
                    break
            bd.baseDonn.commit()
            bd.cursor.close()
            bd.baseDonn.close()

        def quitter():
            showinfo("Alerte", "MERCI DE VOTRE VISITE.A BIENTOT")
            master.quit()

        self.actionBtn_1 = Button(master, text="LISTE DES PRODUITS", width=18,
                         height=2, command=recupere).place(x=10, y=200)
        self.actionBtn_2 = Button(master, text="SUBSTITUS ENREGISTRES", width=20,
                         height=2, command=save).place(x=710, y=200)
        self.actionBtn_3 = Button(master, text="QUITTER", width=15,
                         height=2, command=quitter).place(x=330, y=550)
    # actionBtn_4 = Button(root, text="ENREGISTRER", width=15,
    #                      height=2, command=quitter).place(x=320, y=470)


    

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()