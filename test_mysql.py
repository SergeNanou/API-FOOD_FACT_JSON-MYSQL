
import regex as re
import mysql.connector

from unittest import mock
from app import *
from general_variable import *


@mock.patch('app.exec_mysql_1')
def test_run_q_1(mysql_mock):
    run_q_1()
    mysql_mock.assert_called_with('SELECT DISTINCT p.name_product \
                       FROM Product AS P  WHERE(p.code_bar IN \
                       (SELECT cp.product_code_b FROM Category_product \
                       AS cp WHERE cp.categorie_id IN(SELECT c.id FROM \
                       category AS C WHERE c.name_category = %s))) \
                       ORDER BY RAND()', 'Pizza')
@mock.patch('app.exec_mysql_2')
def test_run_q_2(mysql_mock):
    run_q_2()
    mysql_mock.assert_called_with('SELECT p.name_product, p.description, p.url,s.name_shop \
                                   FROM Product p LEFT JOIN  Category_product AS cp ON  \
                                   p.code_bar = cp.product_code_bar LEFT JOIN Category AS C ON\
                                   c.id = cp.categorie_id LEFT JOIN  shop_product AS sp  ON\
                                   p.code_bar  =  sp.product_code_bar LEFT JOIN Shop AS s ON\
                                   sp.shop_id = s.id  WHERE c.name_category = %s and\
                                   p.nutrition_score = %s ORDER BY RAND()'
                                  , ('Pizza', 'a', ))
@mock.patch('app.exec_mysql_3')
def test_run_q_3(mysql_mock):
    run_q_3()
    mysql_mock.assert_called_with('REPLACE INTO Substitut(name_product, composition, url, product_substitut, category) VALUES (%s, %s, %s, %s, %s, %s)',('La Crazy', 'Farine de blé contient Gluten avec de carbonate de calcium Fer Niacine Thiamine  Eau  Semoule de blé dur contient  Huile dolive vierge extra 0  Levure  Huile de colza  Vinaigre  Farine de blé fermenté déshydrate contient Gluten  Poudre à lever  E450 Bicarbonate soude Phosphate de calcium  Sel  Lait en poudre écrémé','lien: https://fr.openfoodfacts.org/produit/00790956/bases-pizza-marks-spencer','Bases Pizza','Pizza'))
