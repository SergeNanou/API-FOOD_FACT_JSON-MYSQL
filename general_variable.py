import mysql.connector





class GestionBD:

	"""Espace de noms pour les variables et fonctions <pseudo-globales"""
	host = 'localhost'   #
	database = 'Pure_beure' # database name
	user = 'root'   # user name
	password=''  # 
	charset = 'utf8'
	"""Mise en place et interfaçage d'une base de données MySQL"""
	def __init__(self, host, database, user, password,charset):
		"Établissement de la connexion - Création du curseur"
		try:
			self.baseDonn =  mysql.connector.connect(host='localhost',database='Pure_beure',user='root',password='',use_unicode=True,charset ='utf8')


		except Exception as err:
			print ('La connexion avec la base de données a échoué :\n'\
			'Erreur détectée :\n%s' % err)
			self.echec =1
		else:    
			self.cursor = self.baseDonn.cursor(buffered=True)   # création du curseur
			
			self.echec =0