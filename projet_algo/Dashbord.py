from PyQt6.QtWidgets import QApplication,QMainWindow,QLabel,QVBoxLayout,QWidget,QPushButton,QRadioButton,QButtonGroup
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
class Dashbord(QWidget):
    def __init__(self):
        super().__init__()
        self.initalis_Ui()
        self.content_dahsbord()
        #initalise le fenetre de dashbord 
    def initalis_Ui(self):
        screen_gemotry=QApplication.primaryScreen().availableGeometry()
        screen_height=screen_gemotry.height()
        self.setGeometry(0,0,0,screen_height)
        self.setMaximumWidth(250)
        layout=QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        label=QLabel(self)
        label.setStyleSheet("background:black;""margin:0px;""padding:0px")
        layout.addWidget(label)
        self.setLayout(layout)
    # faire le content de dashbord
    def content_dahsbord(self):
        #titre de dashbord
        Label=QLabel("Projet Alogorithme",self)
        Label.setGeometry(40,40,250,30)
        Label.setStyleSheet("color:white;""font-size:20px;""font-family:italic;")
        #icon a cote de titre de dashbord
        label=QLabel(self)
        image=QPixmap("projet/python.png")
        label.setPixmap(image)
        label.setScaledContents(True)
        label.setGeometry(0,40,30,30)
        # button pages accueil
        label_page_dacceuil=QLabel(self)
        image_acceuil=QPixmap("projet/home.png")
        label_page_dacceuil.setPixmap(image_acceuil)
        label_page_dacceuil.setGeometry(20,90,30,30)
        label_page_dacceuil.setScaledContents(True)
        button_return_accueil=QPushButton("Page d'acceuil",self)
        button_return_accueil.setGeometry(60,90,200,30)
        button_return_accueil.setStyleSheet("color:white;""text-align:left;""font-size:15px;""font-family:italic;""background:black;")
        #present les algorithme demande dans le projet pour learn about de algorithme 
        titre_learn=QLabel("learn ALgorithme",self)
        titre_learn.setGeometry(60,140,200,30)
        titre_learn.setStyleSheet("color:white;""font-size:15px;""font-family:italic;")
        image_pixmap=QPixmap("projet/learn.png")
        label_images_learn=QLabel(self)
        label_images_learn.setPixmap(image_pixmap)
        label_images_learn.setScaledContents(True)
        label_images_learn.setGeometry(20,140,30,30)
        # a menu de chosire de quelle algorithe de quelle peut leran about
        radio1_tas_fibo=QRadioButton("Tas de Fibonacci",self)
        radio1_tas_fibo.setGeometry(40,180,150,30)
        radio2_B_arbre=QRadioButton("B-ARBRE",self)
        radio2_B_arbre.setGeometry(40,210,150,30)
        self.radio3_DIJIKSTRA=QRadioButton("Dijkstra",self)
        self.radio3_DIJIKSTRA.setGeometry(40,240,150,30)
        self.setStyleSheet("QRadioButton{""color:white;""}")
        #tetse les algortime
        image_teste=QPixmap("projet/teste.png")
        label_teste_images=QLabel(self)
        label_teste_images.setPixmap(image_teste)
        label_teste_images.setGeometry(20,285,30,30)
        label_teste_images.setScaledContents(True)
        titre_teste_algorithme=QLabel("Teste les algorithme",self)
        titre_teste_algorithme.setGeometry(60,285,300,30)
        titre_teste_algorithme.setStyleSheet("color:white;""font-size:15px;""font-family:italic;")
        # radio de teste les algorithme
        radio1_teste_fibo=QRadioButton("Tas de Fibonacci",self)
        radio1_teste_fibo.setGeometry(40,320,150,30)
        radio2_teste_b_arbre=QRadioButton("B-arbre",self)
        radio2_teste_b_arbre.setGeometry(40,350,150,30)
        radio3_testo_DIJIKSTRA=QRadioButton("Dijikstre",self)
        radio3_testo_DIJIKSTRA.setGeometry(40,380,150,30)
        #About
        button_about=QPushButton("About Application",self)
        button_about.setGeometry(60,500,200,30) 
        button_about.setStyleSheet("color:white;""text-align:left;""background:black;""font-size:15px")
        pixamp_about=QPixmap("projet/about.png")
        label_about=QLabel(self)
        label_about.setPixmap(pixamp_about)
        label_about.setGeometry(20,500,30,30)
        label_about.setScaledContents(True)
        #profile de devloper de application
        profile_application=QPushButton("Devlopper Application",self)
        profile_application.setGeometry(60,550,250,30)
        profile_application.setStyleSheet("color:white;""font-size:15px;""font-family:italic;""background:black;""text-align:left;")
        pixmap_develpopper=QPixmap("projet/profile.png")
        label_images_profile=QLabel(self)
        label_images_profile.setPixmap(pixmap_develpopper)
        label_images_profile.setGeometry(20,550,30,30)
        label_images_profile.setScaledContents(True)
        #logo mundiapolis
        pixampmundiapolis=QPixmap("projet/mundiapolis.png")
        label_logo_mudiapolis=QLabel(self)
        label_logo_mudiapolis.setPixmap(pixampmundiapolis)
        label_logo_mudiapolis.setGeometry(20,550,200,200)
        label_logo_mudiapolis.setScaledContents(True)
    


            
            