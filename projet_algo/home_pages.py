import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QLabel,QHBoxLayout,QWidget,QVBoxLayout,QGridLayout,QLineEdit,QPushButton
from PyQt6.QtGui import QIcon,QPixmap,QMovie
from PyQt6.QtCore import QTimer,QTime,Qt
from Dashbord import Dashbord
from nav_bar import Navbar
from footer import footer

class home_pages(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initalis_interface_principal()
    def initalis_interface_principal(self):
       screen_geomtry=QApplication.primaryScreen().availableGeometry()
       screen_widt=screen_geomtry.width()
       screen_height=screen_geomtry.height()
       self.setGeometry(0,0,screen_widt,screen_height)
       self.setWindowTitle("Projet Alogirthme")
       self.setWindowIcon(QIcon("projet/python.png"))
       self.fond()
       self.footer=footer()
       self.footer.setParent(self)
       self.footer.setGeometry(260,670,1085,50)
       self.navbar()
       self.dashbord()
    def navbar(self):
       labe_tite=QLabel(self)
       labe_tite.setGeometry(270,10,1070,50)
       labe_tite.setStyleSheet("background:#86847e;""border:5px #86847e ;"" border-radius:10px;")
       #image logo for projet
       label_logo=QPixmap("projet/home.png")
       self.label_logo=QLabel(self)
       self.label_logo.setPixmap(label_logo)
       self.label_logo.setScaledContents(True)
       self.label_logo.setGeometry(280,20,30,30)
       label_home=QLabel("Home",self)
       label_home.setGeometry(320,20,50,30)
       label_home.setStyleSheet("color:white;""font-size:15px;""font-family:italic")
       label_serch_logo=QPixmap("projet/serch.png")
       self.label_serach=QLabel(self)
       self.label_serach.setPixmap(label_serch_logo)
       self.label_serach.setGeometry(610,20,30,30)
       self.label_serach.setScaledContents(True)
       self.label_line_edit=QLineEdit(self)
       self.label_line_edit.setGeometry(650,17,400,35)
       self.label_line_edit.setPlaceholderText("entre votre serch here")
       self.label_line_edit.setStyleSheet("""QLineEdit{
                                            border:2px solid None;
                                            border-radius:10px;
                                            }
                                          QLineEdit:focus{
                                            color:bleu;
                                          }
                                          
                                          """)
       # about 
       QPixmap_images_about=QPixmap("projet/about.png")
       self.label_image_about=QLabel(self)
       self.label_image_about.setPixmap(QPixmap_images_about)
       self.label_image_about.setGeometry(380,20,30,30)
       self.label_image_about.setScaledContents(True)
       self.about_texte=QLabel("About",self)
       self.about_texte.setGeometry(420,20,100,30)
       self.about_texte.setStyleSheet("color:white;""font-size:15px;""font-family:italic;")
       #pages principal
       
       self.full_texte="    Bienvenu dans AlgoTest : Dijkstra, Tas de Fibonacci et B-Arbres 😊"
       self.current_texte=""
       self.index=0
       self.label_titre=QLabel("",self)
       self.label_titre.setGeometry(410,100,820,40)
       self.label_titre.setStyleSheet("color:black;font-size:26px;font-family:'Roboto';")
       self.timer=QTimer()
       self.timer.timeout.connect(self.updatetexte)
       self.timer.start(110)
       self.robot_welcome_images=QMovie("projet/robot.gif")
       self.robot_welcome_label=QLabel(self)
       self.robot_welcome_label.setMovie(self.robot_welcome_images)
       self.robot_welcome_label.setGeometry(260,60,130,130)
       self.robot_welcome_label.setScaledContents(True)
       self.robot_welcome_images.start()
       #carte de prsente les algorihtme
       #square
       #carte 1 de Dijisktre
       self.carte=QLabel(self)
       self.carte.setStyleSheet("background:#8f9ed1; border:solid 2px #a5a29a ;border-radius:15px")
       self.carte.setGeometry(400,270,220,250)
       self.image_point=QPixmap("projet/point.png")
       self.point_label=QLabel(self)
       self.point_label.setPixmap(self.image_point)
       self.point_label.setGeometry(510,280,100,100)
       self.point_label.setScaledContents(True)
       self.image_dijkstra=QMovie("projet/dijkstra2.gif")
       self.dijkstra_label=QLabel(self)
       self.dijkstra_label.setMovie(self.image_dijkstra)
       self.dijkstra_label.setGeometry(437,230,150,150)
       self.dijkstra_label.setScaledContents(True)
       self.image_dijkstra.start()
       self.titre_dijkstra=QLabel("Algo Dijikstra",self)
       self.titre_dijkstra.setGeometry(458,379,200,30)
       self.titre_dijkstra.setStyleSheet("color:black;font-size:18px;font-family:'Roboto'")
       self.description=QLabel("c'est une méthode de calcul du chemin \n          le plus  court entre un nœud\n              source et tous les autres \n                nœuds d'un réseau",self)
       self.description.setGeometry(410,392,220,100)
       self.description.setStyleSheet("color:white")
       self.putton_dijkstra=QPushButton("Découvert",self)
       self.putton_dijkstra.setGeometry(457,480,100,30)
       self.putton_dijkstra.setStyleSheet("color:black;background:white;font-family:'Roboto';border:solid white 2px; border-radius:15px;")
       #---------------------------------------------
       #carte 2 Tas de fibonaci
       self.carte2=QLabel(self)
       self.carte2.setStyleSheet("background:#a5a29a; border:solid 2px #a5a29a ;border-radius:15px")
       self.carte2.setGeometry(700,270,220,250)
       self.image_point2=QPixmap("projet/point.png")
       self.point_label2=QLabel(self)
       self.point_label2.setPixmap(self.image_point)
       self.point_label2.setGeometry(810,280,100,100)
       self.point_label2.setScaledContents(True)
       self_images_fibonacci=QMovie("projet/dijkstra.gif")
       self_label_images_fibnacii=QLabel(self)
       self_label_images_fibnacii.setMovie(self_images_fibonacci)
       self_label_images_fibnacii.setGeometry(730,230,150,150)
       self_images_fibonacci.start()
       self.titre_fibonacci=QLabel("Tas de Fibnacci",self)
       self.titre_fibonacci.setGeometry(745,380,200,30)
       self.titre_fibonacci.setStyleSheet("color:black;font-size:18px;font-family:'Roboto'")
       self.fibconacci_description=QLabel("  un ensemble d'arbres satisfaisant la\npropriétéde tas-minimum, c'est-à-dire\nque laclé d'un fils est toujours supérieure ou \n             égale à la clé de son père",self)
       self.fibconacci_description.setGeometry(710,392,220,100)
       self.fibconacci_description.setStyleSheet("color:white")
       self.putton_fibo=QPushButton("Découvert",self)
       self.putton_fibo.setGeometry(760,480,100,30)
       self.putton_fibo.setStyleSheet("color:black;background:white;font-family:'Roboto';border:solid white 2px; border-radius:15px;")
       #_-------------------------------------
       #carte_3 B arbre
       self.carte3=QLabel(self)
       self.carte3.setStyleSheet("background:#a587c5; border:solid 2px #a5a29a ;border-radius:15px")
       self.carte3.setGeometry(1000,270,220,250)
       self.arbre_images=QMovie("projet/b_arbre.gif")
       self.label_arbre_images=QLabel(self)
       self.label_arbre_images.setMovie(self.arbre_images)
       self.label_arbre_images.setGeometry(1035,230,150,160)
       self.arbre_images.start()
       self.label_arbre_title=QLabel("Algo B-Arbre",self)
       self.label_arbre_title.setGeometry(1059,380,100,30)
       self.label_arbre_title.setStyleSheet("color:black;font-size:18px;font-family:'Roboto'")
       self.label_arbre_description=QLabel("  Les arbres B sont principalement mis\n     en œuvre dans les mécanismes de\n     gestion de bases de données et de\n                  systèmes de fichiers.",self)
       self.label_arbre_description.setGeometry(1010,390,200,100)
       self.label_arbre_description.setStyleSheet("color:white;")
       self.putton_arbre=QPushButton("Découvert",self)
       self.putton_arbre.setGeometry(1060,480,100,30)
       self.putton_arbre.setStyleSheet("color:black;background:white;font-family:'Roboto';border:solid white 2px; border-radius:15px;")
       #algo teste
       movie_algotste=QMovie("projet/ALGO_TESTE.gif")
       label_movie_algotste=QLabel(self)
       label_movie_algotste.setMovie(movie_algotste)
       label_movie_algotste.setGeometry(1110,460,250,250)
       movie_algotste.start()

       #---------------------------------
       qhbox=QHBoxLayout()
       qhbox.addWidget(self.carte)
       qhbox.addWidget(self.carte2)
       qhbox.addWidget(self.carte3)
       self.setLayout(qhbox)
       #cercle
       #en ligne
       self.time=QLabel(self)
       self.time.setGeometry(1250,18,90,30)
       self.time.setStyleSheet("color:white;font-size:15px")
       self.timer3=QTimer(self)
       self.timer3.timeout.connect(self.update_time)
       self.timer3.start(100)
       #time logo
       self.time_logo=QMovie("projet/time.gif")
       self.time_logo_label=QLabel(self)
       self.time_logo_label.setMovie(self.time_logo)
       self.time_logo.start()
       self.time_logo_label.setGeometry(1204,15,40,40)
       self.time_logo_label.setScaledContents(True)
       
    def update_time(self):
        current_time=QTime.currentTime().toString("hh : mm : ss ")
        self.time.setText(current_time)
    def updatetexte(self):
        if self.index<len(self.full_texte):
            self.current_texte+=self.full_texte[self.index]
            self.label_titre.setText(self.current_texte)
            self.index+=1
        else:
            self.timer.stop()
            
        
    def dashbord(self):
        self.central=QWidget()
        self.setCentralWidget(self.central)
        self.layout=QVBoxLayout()
        self.mon_dashbord=Dashbord()
        self.layout.addWidget(self.mon_dashbord)
        self.layout.setContentsMargins(0,0,0,0)
        self.central.setLayout(self.layout)
        self.mon_dashbord.button_about.clicked.connect(self.devloppeurr)
        self.mon_dashbord.radio3_DIJIKSTRA.toggled.connect(self.ouvriehomepages)
        self.mon_dashbord.radio2_B_arbre.toggled.connect(self.ouvrie_learn_b_arbre)
        self.mon_dashbord.radio2_teste_b_arbre.toggled.connect(self.ouvrireteste_barbre)
        self.mon_dashbord.radio1_tas_fibo.toggled.connect(self.learn_tas)
        self.mon_dashbord.profile_application2.clicked.connect(self.about)
        self.putton_arbre.clicked.connect(self.ouvrireteste_barbre)
    def clear_layout(self):
        while self.layout.count():
            child = self.layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
    def ouvriehomepages(self):
        from learn_dijikstra import learn_dijikstra
        self.dijkstra_window = learn_dijikstra()
        self.dijkstra_window.showMaximized()
        self.close()
    def about(self):
        self.clear_layout()
        from About import About
        self.abouthh=About()
        self.abouthh.showMaximized()
        self.close()
    def devloppeurr(self):
        from About import About
        self.Aboutk=About()
        self.Aboutk.showMaximized()
        self.close()
    def learn_tas(self):
        from tas_fibo_learn import learn_tas_fibo
        self.fibo_learn=learn_tas_fibo()
        self.fibo_learn.showMaximized()
        self.close()
    def ouvrie_learn_b_arbre(self):
        from learn_barbre import learn_barbre
        self.barbre_learn=learn_barbre()
        self.barbre_learn.showMaximized()
        self.close()
    def ouvrireteste_barbre(self):
        from teste_b_arbre import test_barbre
        self.teste_barbe=test_barbre()
        self.teste_barbe.showMaximized()
        self.close()
    def fond(self):
       self.fond=QPixmap("projet/fond.png")
       self.fond_lable=QLabel(self)
       self.fond_lable.setPixmap(self.fond)
       self.fond_lable.setScaledContents(True)
       self.fond_lable.setGeometry(250,0,250,250)
       self.fond2=QPixmap("projet/fond.png")
       self.fond_lable2=QLabel(self)
       self.fond_lable2.setPixmap(self.fond)
       self.fond_lable2.setScaledContents(True)
       self.fond_lable2.setGeometry(500,0,250,250)
       self.fond3=QPixmap("projet/fond.png")
       self.fond_lable3=QLabel(self)
       self.fond_lable3.setPixmap(self.fond)
       self.fond_lable3.setScaledContents(True)
       self.fond_lable3.setGeometry(750,0,250,250)
       self.fond4=QPixmap("projet/fond.png")
       self.fond_lable4=QLabel(self)
       self.fond_lable4.setPixmap(self.fond)
       self.fond_lable4.setScaledContents(True)
       self.fond_lable4.setGeometry(1000,0,250,250)
       self.fond5=QPixmap("projet/fond.png")
       self.fond_lable5=QLabel(self)
       self.fond_lable5.setPixmap(self.fond)
       self.fond_lable5.setScaledContents(True)
       self.fond_lable5.setGeometry(1250,0,250,250)
       self.fond6=QPixmap("projet/fond.png")
       self.fond_lable6=QLabel(self)
       self.fond_lable6.setPixmap(self.fond)
       self.fond_lable6.setScaledContents(True)
       self.fond_lable6.setGeometry(250,250,250,250)
       self.fond7=QPixmap("projet/fond.png")
       self.fond_lable7=QLabel(self)
       self.fond_lable7.setPixmap(self.fond)
       self.fond_lable7.setScaledContents(True)
       self.fond_lable7.setGeometry(500,250,250,250)
       self.fond8=QPixmap("projet/fond.png")
       self.fond_lable8=QLabel(self)
       self.fond_lable8.setPixmap(self.fond)
       self.fond_lable8.setScaledContents(True)
       self.fond_lable8.setGeometry(750,250,250,250)
       self.fond9=QPixmap("projet/fond.png")
       self.fond_lable9=QLabel(self)
       self.fond_lable9.setPixmap(self.fond)
       self.fond_lable9.setScaledContents(True)
       self.fond_lable9.setGeometry(1000,250,250,250)
       self.fond10=QPixmap("projet/fond.png")
       self.fond_lable10=QLabel(self)
       self.fond_lable10.setPixmap(self.fond)
       self.fond_lable10.setScaledContents(True)
       self.fond_lable10.setGeometry(1250,250,250,250)
       self.fond11=QPixmap("projet/fond.png")
       self.fond_lable11=QLabel(self)
       self.fond_lable11.setPixmap(self.fond)
       self.fond_lable11.setScaledContents(True)
       self.fond_lable11.setGeometry(500,500,250,250)
       self.fond12=QPixmap("projet/fond.png")
       self.fond_lable12=QLabel(self)
       self.fond_lable12.setPixmap(self.fond)
       self.fond_lable12.setScaledContents(True)
       self.fond_lable12.setGeometry(750,500,250,250)
       self.fond13=QPixmap("projet/fond.png")
       self.fond_lable13=QLabel(self)
       self.fond_lable13.setPixmap(self.fond)
       self.fond_lable13.setScaledContents(True)
       self.fond_lable13.setGeometry(1000,500,250,250)
       self.fond14=QPixmap("projet/fond.png")
       self.fond_lable14=QLabel(self)
       self.fond_lable14.setPixmap(self.fond)
       self.fond_lable14.setScaledContents(True)
       self.fond_lable14.setGeometry(1250,500,250,250)
       self.fond15=QPixmap("projet/fond.png")
       self.fond_lable15=QLabel(self)
       self.fond_lable15.setPixmap(self.fond)
       self.fond_lable15.setScaledContents(True)
       self.fond_lable15.setGeometry(250,500,250,250)
def main():
    app=QApplication(sys.argv)
    window=home_pages()
    window.show()
    window.showMaximized()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

        